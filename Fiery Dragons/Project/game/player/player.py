from abc import ABC

import pygame
from pygame import Vector2

from math import sin

from game.enums.playertypes import PlayerTypes
from engine.animation import Animation
from engine.sprite import Sprite
from engine.state import State
from engine.utils import lengthdir_x, lengthdir_y
from game.cave import Cave
from game.tile import Tile


class Player(Sprite, ABC, State):
    """
    Author: Yash Mahmud (32945795)

    A class used to represent a Player, which is a subclass of Sprite.

    ...

    Attributes
    ----------
    board : Board
        The board on which the Player is placed.
    origin : Vector2
        The origin of the player.
    pos : Tile
        The current position of the player.
    cave : Cave
        The starting position of the player.
    steps : int
        The number of steps the player has taken.
    player_id : int
        The id of the player.

    Methods
    -------
    __init__(origin, start_tile, player_id):
        Constructs all the necessary attributes for the player object.
    __str__():
        Returns a string representation of the player.
    move(board, pos):
        Moves the player to a new position on the board.
    get_tile():
        Returns the current position of the player.
    get_is_in_cave():
        Returns True if the player is in a cave, False otherwise.
    get_cave():
        Returns the cave the player is in.
    save(data):
        Saves the state of the Token.
    load(data):
        Loads the state of the Token.
    """

    def __init__(self, board, origin: pygame.Vector2, start_tile: Tile, player_id: int, player_type: PlayerTypes = None):
        """
        Author: Yash Mahmud (32945795)

        Constructs all the necessary attributes for the player object.

        Parameters
        ----------
            board : Board
                the board on which the player is placed
            origin : Vector2
                a tuple representing the origin of the player (x, y)
            start_tile : Tile
                the starting position of the player
            player_id : int
                the id of the player
            player_type : PlayerTypes
                the type of the player
        """

        self.board = board
        self.player_type = player_type
        self.origin = origin
        super().__init__(origin[0], origin[1], "dragons/dragon_" + str(player_id), (0.15, 0.15))

        tints = [(193, 54, 54, 255), (107, 193, 255, 255), (255, 216, 0, 255), (89, 175, 99, 255)]

        self.currentTile = start_tile
        self.cave = start_tile.get_cave()
        self.currentTile.occupant = None

        self.steps = 0
        self.move_to = self.currentTile.cave.pos + Vector2(lengthdir_x(60, self.currentTile.cave.angle),
                                                           lengthdir_y(60, self.currentTile.cave.angle))

        self.select_animation = Animation([1+(abs(sin(i/10))/2) for i in range(32)], 1, True)
        self.select_animation.play_animation()

        self.player_id = player_id
        self.cave.set_tint(tints[self.player_id])

        self.in_cave = True

    def __str__(self) -> str:
        """
        Author: Yash Mahmud (32945795)

        Returns a string representation of the player.

        Returns
        -------
            str
                a string representation of which player is playing
        """
        return "Player {0}".format((self.player_id + 1))

    def update(self) -> None:
        """
        Author: Yash Mahmud (32945795)

        Updates the player's position on the board.
        """

        if self.pos != self.move_to:
            self.set_position_smooth(self.move_to, 0.1)

        if self.board.current_player == self:
            self.select_animation.update()
            self.set_scale(0.15 * self.select_animation.get_current_frame(), 0.15 * self.select_animation.get_current_frame())
        else:
            self.set_scale(0.15, 0.15)

    def move(self, pos: int) -> None:
        """
        Author: Yash Mahmud (32945795)

        Moves the player to a new position on the board.

        Parameters
        ----------
            pos : int
                the new position of the player
        """
        if self.steps + pos > len(self.board) + 2:
            self.board.switch_player()
            return

        if self.steps + pos == len(self.board) + 2:
            self.in_cave = True
            self.currentTile.occupant = None
            self.board.winner = self
            return

        tile_id = self.currentTile.get_tile_id()
        new_tile = self.board.get_tile((tile_id + pos) % len(self.board))

        if self.in_cave and self.steps == 0:
            self.in_cave = False
            tile_id = (self.cave.next_tile + pos - 1) % len(self.board)
            new_tile = self.board.get_tile(tile_id)

        self.currentTile.occupant = None

        self.currentTile = new_tile
        self.currentTile.occupant = self

        # Tile movement code
        self.move_to = new_tile.pos + Vector2(lengthdir_x(60, new_tile.angle), lengthdir_y(60, new_tile.angle))

        self.steps += pos

    def move_to_tile(self, tile: Tile) -> None:
        """
        Author: Yash Mahmud (32945795)

        Moves the player to a new tile on the board.

        Parameters
        ----------
            tile : Tile
                the new tile the player will move to
        """
        self.currentTile.occupant = None
        self.currentTile = tile
        self.currentTile.occupant = self

        if self.in_cave:
            self.move_to = tile.cave.pos + Vector2(lengthdir_x(60, self.currentTile.cave.angle),
                                                   lengthdir_y(60, self.currentTile.cave.angle))
        else:
            self.move_to = tile.pos + Vector2(lengthdir_x(60, tile.angle),
                                              lengthdir_y(60, tile.angle))

    def get_tile(self) -> Tile:
        """
        Author: Yash Mahmud (32945795)

        Returns the current position of the player.

        Returns
        -------
            Tile
                the current position of the player
        """
        return self.currentTile

    def get_is_in_cave(self) -> bool:
        """
        Author: Yash Mahmud (32945795)

        Returns True if the player is in a cave, False otherwise.

        Returns
        -------
            bool
                True if the player is in a cave, False otherwise
        """
        return self.in_cave

    def get_cave(self):
        """
        Author: Yash Mahmud (32945795)

        Returns the cave the player is in.

        Returns
        -------
            Cave
                the cave the player is in
        """
        return self.cave

    def save(self, data):
        """
        Author: Yash Mahmud (32945795)

        Saves the state of the Token.

        Parameters
        ----------
            data : dict
                the dictionary to save the Token state to
        """
        player_data = {
            'x': str(self.pos.x),
            'y': str(self.pos.y),
            'steps': self.steps,
            'in_cave': self.in_cave
        }
        data['player_' + str(self.player_id)] = player_data

    def load(self, data):
        """
        Author: Yash Mahmud (32945795)

        Loads the state of the Token.

        Parameters
        ----------
            data : dict
                the dictionary to load the Token state from
        """
        player_data = data['player_' + str(self.player_id)]
        self.in_cave = player_data['in_cave']
        self.steps = player_data['steps']
        print(self.player_id, self.steps, self.in_cave, self.cave)
        if self.in_cave:
            new_tile = self.board.get_tile(self.get_cave().next_tile)
        else:
            new_tile = self.board.get_tile(
                (self.steps - 1 + ((len(self.board) // 4) * self.player_id)) % len(self.board))

        self.currentTile.occupant = None
        self.currentTile = new_tile
        self.currentTile.occupant = self

        if self.in_cave:
            self.move_to = new_tile.cave.pos + Vector2(lengthdir_x(60, self.currentTile.cave.angle),
                                                       lengthdir_y(60, self.currentTile.cave.angle))
               
            self.currentTile.occupant = None
        else:
            self.move_to = new_tile.pos + Vector2(lengthdir_x(60, new_tile.angle),
                                                  lengthdir_y(60, new_tile.angle))
        self.set_position(Vector2(float(player_data['x']), float(player_data['y'])))
