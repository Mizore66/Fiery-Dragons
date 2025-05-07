from engine.sprite import Sprite
from game.buttons.cpu_button import CPUButton
from game.buttons.difficulty_button import DifficultyButton
from game.buttons.quit_game_button import QuitGameButton
from game.buttons.start_game_button import StartGameButton
from game.scene import Scene

from pygame_gui import UIManager
from pygame import time


class MainMenu(Scene):
    """
    Author: Yash Mahmud (32945795)

    A class used to represent a MainMenu, which is a subclass of Scene.

    ...

    Attributes
    ----------
    game : Game
        The game object.
    origin : Vector2
        The origin position of the main menu to render.
    manager : UIManager
        The manager for the UI elements.
    background : Sprite
        The background of the main menu.
    game_logo : Sprite
        The game logo of the main menu.
    start_button : StartGameButton
        The start game button of the main menu.
    diff_button : DifficultyButton
        The difficulty button of the main menu.
    cpu_button : CPUButton
        The CPU button of the main menu.
    quit_button : QuitGameButton
        The quit game button of the main menu.

    Methods
    -------
    update():
        Updates the main menu.
    draw(surface):
        Draws the main menu on the provided surface.
    events(event):
        Handles the events for the main menu.
    set_difficulty(difficulty):
        Sets the difficulty of the game.
    set_cpu_count(cpu):
        Sets the number of CPUs in the game.
    """
    def __init__(self, game, origin):
        """
        Author: Yash Mahmud (32945795)

        Constructs all the necessary attributes for the MainMenu object.

        Parameters
        ----------
            game : Game
                The game object.
            origin : Vector2
                The origin position of the main menu to render.
        """
        self.manager = UIManager(game.SCREEN_SIZE, theme_path="assets/theme.json")

        self.origin = origin
        self.game = game

        self.background = Sprite(origin.x, origin.y, "/ui/sprBackground", (1, 1), 0)
        self.game_logo = Sprite(origin.x, origin.y - 100, "/ui/sprFieryDragonsLogo", (0.75, 0.75), 0)

        self.start_button = StartGameButton(self.manager, origin.x - 200/2, origin.y + 150, (200, 50), 0, game, origin)
        self.diff_button = DifficultyButton(self.manager, origin.x - 200/2, origin.y + 200, (200, 50), 0, self)
        self.cpu_button = CPUButton(self.manager, origin.x - 200/2, origin.y + 250, (200, 50), 0, self, 0)
        self.quit_button = QuitGameButton(self.manager, origin.x - 200/2, origin.y + 300, (200, 50), 0, game)

    def update(self):
        """
        Author: Yash Mahmud (32945795)

        Updates the main menu.
        """
        self.manager.update(time.get_ticks() / 1000.0)

    def draw(self, surface):
        """
        Author: Yash Mahmud (32945795)

        Draws the main menu on the provided surface.

        Parameters
        ----------
            surface : Surface
                the surface to draw the main menu on
        """
        self.background.draw(surface)
        self.game_logo.draw(surface)
        self.manager.draw_ui(surface)

    def events(self, event):
        """
        Author: Yash Mahmud (32945795)

        Handles the events for the main menu.

        Parameters
        ----------
            event : Event
                the event to handle
        """
        self.start_button.events(event)
        self.quit_button.events(event)
        self.diff_button.events(event)
        self.cpu_button.events(event)

        self.manager.process_events(event)

    def set_difficulty(self, difficulty):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Sets the difficulty of the game.

        Parameters
        ----------
            difficulty : int
                the difficulty of the game
        """
        self.start_button.set_difficulty(difficulty)

    def set_cpu_count(self, cpu):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Sets the number of CPUs in the game.

        Parameters
        ----------
            cpu : int
                the number of CPUs in the game
        """
        self.start_button.set_cpu_count(cpu)
