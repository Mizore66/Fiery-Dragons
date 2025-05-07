from abc import abstractmethod

import pygame
from enum import Enum

from pygame import Surface

from engine.sprite import Sprite


class ClickState(Enum):
    """
    An enumeration class for the different states of a button click.

    Author: Yash Mahmud (32945795)

    Attributes
    ----------
    CLICK : int
        Represents the state when the button is clicked.
    HOLD : int
        Represents the state when the button is held down.
    RELEASE : int
        Represents the state when the button is released.
    """
    CLICK = 1
    HOLD = 2
    RELEASE = 3


class Button(Sprite):
    """
    A class used to represent a Button, which is a subclass of Sprite.

    Author: Yash Mahmud (32945795)
    ...

    Attributes
    ----------
    click_state : ClickState
        The current state of the button click.
    clicked : bool
        A flag indicating whether the button is clicked or not.

    Methods
    -------
    draw(surface):
        Draws the button on the given surface.
    update():
        Updates the state of the button based on mouse events.
    on_click():
        Abstract function that defines what happens when the button is clicked.
    on_hold():
        Abstract function that Defines what happens when the button is held down.
    on_release():
        Abstract function that Defines what happens when the button is released.
    """

    def __init__(self, x: int, y: int, image: str, scale: tuple = (1, 1), angle: int = 0):
        """
        Author: Yash Mahmud (32945795)

        Constructs all the necessary attributes for the button object.

        Parameters
        ----------
            x : int
                x-coordinate of the button
            y : int
                y-coordinate of the button
            image : str
                the filename of the button image
            scale : int, optional
                the scale of the button (default is 1)
            angle : int, optional
                the angle of the button (default is 0)
        """
        super().__init__(x, y, image, scale, angle)
        self.click_state = ClickState.RELEASE
        self.clicked = False

    def draw(self, surface: Surface) -> None:
        """
        Author: Yash Mahmud (32945795)

        Draws the button on the given surface.

        Parameters
        ----------
            surface : Surface
                the surface to draw the button on
        """
        super().draw(surface)

    def update(self) -> bool:
        """
        Author: Yash Mahmud (32945795)

        Updates the state of the button based on mouse events.

        Returns
        -------
            bool
                True if the button is clicked, False otherwise.
        """
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.clicked = pygame.mouse.get_pressed()[0]

            if self.clicked:
                if self.click_state == ClickState.RELEASE:
                    self.click_state = ClickState.CLICK
                    self.on_click()
                    return self.clicked

                if self.click_state == ClickState.CLICK:
                    self.click_state = ClickState.HOLD

                if self.click_state == ClickState.HOLD:
                    self.on_hold()
            else:
                if not self.click_state == ClickState.RELEASE:
                    self.click_state = ClickState.RELEASE
                    self.on_release()

        return self.clicked

    @abstractmethod
    def on_click(self) -> None:
        """
        Author: Yash Mahmud (32945795)

        Defines what happens when the button is clicked.
        This method should be overridden in a subclass.
        """
        pass

    @abstractmethod
    def on_hold(self) -> None:
        """
        Author: Yash Mahmud (32945795)

        Defines what happens when the button is held down.
        This method should be overridden in a subclass.
        """
        pass

    @abstractmethod
    def on_release(self) -> None:
        """
        Author: Yash Mahmud (32945795)
        
        Defines what happens when the button is released.
        This method should be overridden in a subclass.
        """
        pass
