from abc import ABC

import pygame_gui
import pygame
from pygame import Vector2

from engine.button import Button
from game.enums.difficultytypes import DifficultyType
from game.game_session import GameSession


class StartGameButton(Button, ABC):
    """
    Author: Yash Mahmud (32945795)

    A class used to represent a StartGameButton, which is a subclass of Button.

    ...

    Attributes
    ----------
    manager : UIManager
        the manager for the button
    game : Game
        the game to start
    origin : Vector2
        the origin of the game
    difficulty : DifficultyType
        the difficulty of the game
    cpu_count : int
        the number of CPUs in the game
    button : UIButton
        the button to start the game

    Methods
    -------
    events(event):
        Handles the events for the button.
    """
    def __init__(self, manager, x: int, y: int, size: tuple, angle: int, game, origin: Vector2,
                 difficulty: DifficultyType = DifficultyType.EASY, cpu_count: int = 0):
        """
        Author: Yash Mahmud (32945795)

        Constructs all the necessary attributes for the StartGameButton object.

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
                the game to start
            origin : Vector2
                the origin of the game
            difficulty : DifficultyType
                the difficulty of the game
            cpu_count : int
                the number of CPUs in the game
        """
        self.manager = manager
        self.game = game
        self.origin = origin
        self.difficulty = difficulty
        self.cpu_count = cpu_count

        self.button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(x, y, size[0], size[1]),
                                                   text='Start Game',
                                                   manager=self.manager)

    def set_difficulty(self, difficulty):
        """
        Author: Yash Mahmud (32945795)

        Sets the difficulty of the game.

        Parameters
        ----------
        difficulty : DifficultyType
            the difficulty of the game
        """
        self.difficulty = difficulty

    def set_cpu_count(self, cpu_count):
        """
        Author: Yash Mahmud (32945795)

        Sets the number of CPUs in the game.

        Parameters
        ----------
        cpu_count : int
            the number of CPUs in the game
        """
        self.cpu_count = cpu_count

    def events(self, event):
        """
        Author: Yash Mahmud (32945795)

        Handles the events for the button.

        Parameters
        ----------
        event : UIEvent
            the event to handle
        """
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.button:
                self.game.change_scene(GameSession(self.game, self.origin, self.difficulty, self.cpu_count))
