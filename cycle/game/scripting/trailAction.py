from game.scripting.action import Action

class MakeTrailAction(Action):
    """
    An update action that increases the players trail.
    
    The responsibility of Make trail action is to increase the trial of the players
    """
# Edit this
    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            
        """
        cyclists = cast.get_actors("cyclists")
        for cyclist in cyclists:
            cyclist.grow_tail(1)