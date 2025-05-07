from abc import ABC

import pygame
import pygame_gui
from pygame import Color

from engine.button import Button
from engine.text import Text


class QuitGameButton:
    """
    Author: Yash Mahmud (32945795)

    A class used to represent a QuitGameButton, which is a subclass of Button.

    ...

    Attributes
    ----------
    game : Game
        the game to quit
    manager : UIManager
        the manager for the button
    button : UIButton
        the button to quit the game

    Methods
    -------
    events(event):
        Handles the events for the button.
    """
    def __init__(self, manager, x: int, y: int, size: tuple, angle: int, game):
        """
        Author: Yash Mahmud (32945795)

        Constructs all the necessary attributes for the QuitGameButton object.

        Parameters
        ----------
            manager : UIManager
                the manager for the button
            x : int
                x-coordinate of the button
            y : int
                y-coordinate of the button
            size : tuple
                the size of the button
            angle : int
                the angle of the button
            game : Game
                the game to quit
        """
        self.game = game
        self.manager = manager

        self.button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(x, y, size[0], size[1]),
                                                         text='Quit',
                                                         manager=self.manager)

    def events(self, event):
        """
        Author: Yash Mahmud (32945795)

        Handles the events for the button.

        Parameters
        ----------
            event : Event
                the event to handle
        """
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.button:
                self.game.quit()
