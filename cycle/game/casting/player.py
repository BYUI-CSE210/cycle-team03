import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Player(Actor):
    """
    A long limbless reptile that represents a player.
    
    The responsibility of Player is to move itself.

    Attributes:
        _segments (list): A list containing the segments of the player (reptile)
    """
    def __init__(self, player_position = 1):
        super().__init__()
        self._segments = []
        self._player_position = player_position
        self._player_color = constants.RED
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for _ in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.GREEN)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        if self._player_position == 1:
            x = int(constants.MAX_X / 4.5)
            color = self._player_color()
        else:
            x = int(constants.MAX_X - (constants.MAX_X/ 4.5))

        y = int(constants.MAX_Y / 3)

        for i in range(constants.PLAYER_LENGTH):
            position = Point(x , y + i * constants.CELL_SIZE)
            velocity = Point(0, -constants.CELL_SIZE)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)