from pygame import Rect
import pygame_gui

from engine.button import Button
from abc import ABC

from game.buttons.save_window import SaveWindow


class SaveButton(Button, ABC):
    """
    Author: Yash Mahmud (32945795)

    A class used to represent a SaveButton, which is a subclass of Button.

    ...

    Attributes
    ----------
    board : Board
        the board to save
    manager : UIManager
        the manager for the button
    button : UIButton
        the button to save the board

    Methods
    -------
    events(event):
        Handles the events for the button.
    """
    def __init__(self, manager, x: int, y: int, size: tuple, angle: int, board, game_session):
        """
        Author: Yash Mahmud (32945795)

        Constructs all the necessary attributes for the SaveButton object.

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
            board : Board
                the board to save
            game_session : GameSession
                the game session for the button
        """
        self.board = board
        self.manager = manager
        self.game_session = game_session
        self.button = pygame_gui.elements.UIButton(relative_rect= Rect(x, y, size[0], size[1]),
                                                   text='Save/Load',
                                                   manager=self.manager)

    def events(self, event):
        """
        Author: Yash Mahmud (32945795)

        Handles the events for the button.

        Parameters
        ----------
        event : Event
            a pygame event
        """
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.button:
                self.game_session.save_window = SaveWindow(self.manager, self.board.origin.x - 600/2, self.board.origin.y - 400/2, (600, 400), self.board)
                self.board.window_open = True
