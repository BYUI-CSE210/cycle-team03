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

    def _handle_collision(self, cast):
        """Updates the score.
        
        Args:
            cast (Cast): The cast of the Actors in the game.
        """
        score = cast.get_first_actor("scores")
        # food = cast.get_first_actor("foods")
        # snake = cast.get_first_actor("snakes")
        # head = snake.get_head()

        # if head.get_position().equals(food.get_position()):
        #     points = food.get_points()
        #     snake.grow_tail(points)
        #     score.add_points(points)
        #     food.reset()

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if a player collides with one of one of its own segments or the other players segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        trail = cast.get_first_actor("cyclist")
        head = trail.get_segments()[0]
        segments = trail.get_segments()[1:]

        cyclist = cast.get_actors("cyclist")
        cyclist_1 = cyclist[0]
        cyclist_2 = cyclist[1]
        cyclist_1_segment = cyclist_1.get_segment()
        cyclist_2_segment = cyclist_2.get_segment()
        cyclist_1_head = cyclist_1.get_head()
        cyclist_2_head = cyclist_2.get_head()

        for segment in cyclist_1_segment:
            if cyclist_2_head.get_position().equals(segment.get_position()):
                self._is_game_over = True

        for segment in cyclist_2_segment:
            if cyclist_1_head.get_position().equals(segment.get_position()):
                self._is_game_over = True

    def _handle_game_over(self, cast):
        """Shows the 'Game Over' message and turns the losing cyclist white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            trail = cast.get_first_actor("cyclist")
            segments = trail.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("GAME OVER!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            
