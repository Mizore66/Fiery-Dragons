from abc import ABC
import pygame
from pygame import Color, time, Vector2
from pygame_gui import UIManager

from engine.sprite import Sprite
from engine.text import Text
from engine.utils import play_music
from game.board import Board
from game.buttons.save_button import SaveButton
from game.enums.difficultytypes import DifficultyType
from game.scene import Scene
from game.timer import Timer


class GameSession(Scene, ABC):
    """
    Author: Yash Mahmud (32945795)

    A class used to represent a GameSession, which is a subclass of Scene.

    ...

    Attributes
    ----------
    game : Game
        The game object.
    origin : Vector2
        The origin position of the game session to render.
    difficulty : DifficultyType
        The difficulty level of the game.
    cpu_count : int
        The number of CPUs in the game.
    board : Board
        The board of the game.
    manager : UIManager
        The manager for the UI elements.
    background : Sprite
        The background of the game.
    winner_text : Text
        The text for the winner.
    timer_text : Text
        The text for the timer.
    break_timer_text : Text
        The text for the break timer.
    break_time_text : Text
        The text for the break time.
    game_timer : Timer
        The timer for the game.
    save_button : SaveButton
        The save button for the game.
    save_window : None
        The window for the save button.

    Methods
    -------
    update():
        Updates the game session.
    draw(surface):
        Draws the game session on the provided surface.
    events(event):
        Processes the events for the game session.
    pause_game():
        Pauses the game during the break.
    """

    def __init__(self, game, origin, difficulty: DifficultyType = DifficultyType.EASY, cpu_count: int = 0):
        """
        Constructs all the necessary attributes for the GameSession object.
        
        Parameters
        ----------
        game : Game
            The game object.
        origin : Vector2
            The origin position of the game session to render.
        difficulty : DifficultyType
            The difficulty level of the game.
        cpu_count : int
            The number of CPUs in the game.
        """
        self.manager = UIManager(game.SCREEN_SIZE, theme_path="assets/theme.json")
        self.game = game
        self.origin = origin
        self.difficulty = difficulty
        self.cpu_count = cpu_count
        self.board = Board(origin, self.difficulty, self.cpu_count)
        play_music("musBackground")

        self.background = Sprite(origin.x, origin.y, "/ui/sprBackground", (1, 1), 0)
        self.winner_text = Text("", self.origin, Color(255, 0, 0), "calist", "center")
        self.timer_text = Text("", Vector2(self.origin.x * 2 - 20, 20), Color(255, 255, 255), "calist", "topright")
        self.break_timer_text = Text("", Vector2(self.origin.x * 2 - 20, 20), Color(255, 0, 0), "calist", "topright")
        self.break_time_text = Text("Break Time", self.origin, Color(255, 0, 0), "calist", "center")

        # set up the timer for
        self.game_timer = Timer(1500, 300) # Author: Chua Xian Loong (32669747)
        # 1500 seconds (25 minutes) game time, 300 seconds (5 minutes) break interval
        self.game_timer.activate() # Author: Chua Xian Loong (32669747)

        self.save_button = SaveButton(self.manager, 50, origin.y * 2 - 100, (150, 50), 0, self.board, self)
        self.save_window = None

    def update(self):
        """
        Author: Yash Mahmud (32945795)

        Updates the game session.
        """

        self.game_timer.update() # Author: Chua Xian Loong (32669747)

        if self.game_timer.on_break:
            return

        self.board.update()

        if self.board.get_finished():
            return

        if self.board.winner_check():
            self.winner_text.set_text(str(self.board.winner_check()) + " is the winner.")

        self.manager.update(time.get_ticks() / 1000.0)

    def draw(self, surface):
        """
        Author: Yash Mahmud (32945795)

        Draws the game session on the provided surface.

        Parameters
        ----------
            surface : Surface
                the surface to draw the session objects on.
        """
        self.background.draw(surface)

        self.board.draw(surface)

        if self.board.get_finished():
            self.winner_text.draw(surface)

        # Author: Chua Xian Loong (32669747)
        elif not self.game.running:
            time_up_text = Text("Time's up!", self.origin, Color(255, 0, 0), "arial", "center")
            time_up_text.draw(surface)

        # Author: Chua Xian Loong (32669747)
        if self.game_timer.on_break:
            self.break_timer_text.set_text(self.game_timer.get_break_time_left())
            self.break_timer_text.draw(surface)
            self.break_time_text.draw(surface)
            return
        elif self.game_timer.active:
            self.timer_text.set_text(self.game_timer.get_remaining_time())
            self.timer_text.draw(surface)

        self.manager.draw_ui(surface)

    def events(self, event):
        """
        Author: Yash Mahmud (32945795)

        Processes the events for the game session.

        Parameters
        ----------
            event : Event
                the event to process.
        """

        if self.board.get_finished():
            return

        # Author: Chua Xian Loong (32669747)
        if self.game_timer.on_break:
            self.pause_game()

            return

        self.save_button.events(event)
        if self.save_window is not None:
            self.save_window.events(event)
        self.manager.process_events(event)

    def pause_game(self):
        """
        Author: Chua Xian Loong (32669747)
        
        Pauses the game during the break.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                return
