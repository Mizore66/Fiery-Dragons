import pygame
from pygame import Vector2

from engine.text import Text
from game.board import Board
from engine.utils import toggle_music
from game.main_menu import MainMenu


class Game:
    """
        Author: Yash Mahmud (32945795)

        A class used to represent a Game.

        ...

        Attributes
        ----------
        running : bool
            A flag indicating whether the game is running.
        SCREEN_SIZE : Vector2
            The size of the game screen.
        SCREEN_CENTER : Vector2
            The center of the game screen.
        screen : Surface
            The game screen.
        board : Board
            The game board.
        finished : bool
            A flag indicating whether the game is finished.
        clock : Clock
            The game clock.
        winner_text : Text
            The text displaying the winner of the game.

        Methods
        -------
        __init__():
            Constructs all the necessary attributes for the game object.
        draw():
            Draws the game on the screen.
        update():
            Updates the state of the game.
        events():
            Handles the game events.
        run():
            Runs the game.
        change_scene(scene):
            Changes the current scene to the provided scene.
        quit():
            Quits the game.
        """

    def __init__(self):
        """
        Author: Yash Mahmud (32945795)

        Constructs all the necessary attributes for the game object.
        """
        pygame.init()
        pygame.mixer.init()

        self.running = True

        self.SCREEN_SIZE = Vector2(1200, 800)
        self.SCREEN_CENTER = self.SCREEN_SIZE // 2

        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)

        pygame.display.set_caption("Fiery Dragons")

        self.current_scene = MainMenu(self, self.SCREEN_CENTER)

        pygame.key.set_repeat()

        self.clock = pygame.time.Clock()

    def draw(self) -> None:
        """
        Author: Yash Mahmud (32945795)

        Draws the game on the screen.
        """

        self.screen.fill((202, 228, 241))

        self.current_scene.draw(self.screen)

    def update(self) -> None:
        """
        Author: Yash Mahmud (32945795)

        Updates the state of the game.
        """

        self.clock.tick(60)

        self.current_scene.update()

    def events(self) -> None:
        """
        Author: Yash Mahmud (32945795)

        Handles the game events.
        """

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_F1:
                    toggle_music()

            self.current_scene.events(event)

        return

    def run(self) -> None:
        """
        Author: Yash Mahmud (32945795)

        Runs the game.
        """
        while self.running:
            self.clock.tick(120)

            self.events()

            self.update()

            self.draw()

            pygame.display.update()

    def change_scene(self, scene):
        """
        Author: Yash Mahmud (32945795)

        Changes the current scene to the provided scene.
        """
        self.current_scene = scene

    def quit(self):
        """
        Author: Yash Mahmud (32945795)

        Quits the game.
        """
        self.running = False
