from operator import concat
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False 

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)


    def _handle_segment_collision(self, cast):
        """Sets the game over flag if a player collides with one of one of its own segments or the other players segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cyclists = cast.get_actors("cyclists")
        cyclist_1_head = cyclists[0].get_head()
        cyclist_2_head = cyclists[1].get_head()
        cyclist_1_segments = cyclists[0].get_segments()[1:]
        cyclist_2_segments = cyclists[1].get_segments()[1:]

        scores = cast.get_actors("scores")
        
        for segment in cyclist_1_segments:
            if cyclist_2_head.get_position().equals(segment.get_position()):
                scores[1].add_points(1)
                self._is_game_over = True

        for segment in cyclist_2_segments:
            if cyclist_1_head.get_position().equals(segment.get_position()):
                scores[0].add_points(1)
                self._is_game_over = True



    def _handle_game_over(self, cast):
        """Shows the 'Game Over' message and turns the losing cyclist white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cyclists = cast.get_actors("cyclists")
            cyclist_1_segments = cyclists[0].get_segments()
            cyclist_2_segments = cyclists[1].get_segments()
            segments = concat(cyclist_1_segments, cyclist_2_segments)

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("GAME OVER!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            for cyclist in cyclists:
                cyclist.set_player_color(constants.WHITE)
            
