from abc import abstractmethod


class Scene:
    """
    Author: Yash Mahmud (32945795)

    An abstract class representing a scene in the game.

    Methods
    -------
    update():
        Updates the scene.
    draw(surface):
        Draws the scene on the given surface.
    events(event):
        Handles the events for the scene.
    """
    @abstractmethod
    def update(self):
        """
        Author: Yash Mahmud (32945795)

        Updates the scene.
        This method should be overridden in a subclass.
        """
        pass

    @abstractmethod
    def draw(self, surface):
        """
        Author: Yash Mahmud (32945795)
        
        Draws the scene on the given surface.
        This method should be overridden in a subclass.

        Parameters
        ----------
            surface : Surface
                The surface to draw the scene on.
        """
        pass

    @abstractmethod
    def events(self, event):
        """
        Author: Yash Mahmud (32945795)

        Handles the events for the scene.

        Parameters
        ----------
            event : Event
                The event to handle.
        """
        pass
