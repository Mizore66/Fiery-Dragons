from abc import ABC

from pygame import Surface, BLEND_RGBA_MULT

from engine.sprite import Sprite
from engine.state import State
from engine.utils import lengthdir_x, lengthdir_y
from game.enums.animaltypes import AnimalType


class Cave(Sprite, ABC, State):
    """
    Represents a Cave which is a subclass of Tile. Each cave has unique properties like its type,
    associated tile, and can contain specific game mechanics related to the game board.

    Author: Yash Mahmud (32945795)

    Attributes
    ----------
    border_sprite : Sprite
        The sprite used for the border or additional decorative elements of the cave.
    tile_type : AnimalType
        The type of animal associated with the cave.
    next_tile : int
        The tile ID that this cave links to or affects in the game logic.
    tint : tuple
        The RGBA color to tint the cave sprite.
    angle: float
        The angle of the cave sprite.

    Methods
    -------
    draw(surface: Surface):
        Draws the cave along with its border on the given surface.
    set_tint(tint: tuple):
        Sets the tint color for the cave sprites to achieve various visual effects.
    get_tile_type() -> AnimalType:
        Returns the type of animal associated with the cave.
    cave_next_tile() -> int:
        Returns the next linked tile's ID.
    save(data: dict):
        Saves the cave's data to a dictionary.
    load(data: dict):
        Loads the cave's data from a dictionary.
    """

    def __init__(self, tile_type: AnimalType, tile, tile_id: int):
        """
        Author: Yash Mahmud (32945795)

        Initializes a new instance of the Cave class.

        Parameters
        ----------
        tile_type : AnimalType
            The animal type associated with the cave.
        tile : Tile
            The tile object that this cave is associated with.
        tile_id : int
            The identifier of the tile which may be affected by the cave.

        The cave's position and scale are calculated based on the tile's properties.
        """
        super().__init__(tile.pos.x + lengthdir_x(100, tile.angle), tile.pos.y + lengthdir_y(100, tile.angle), f"caves/cave_{tile_type.name}", (tile.scale[0] * 0.5, tile.scale[1] * 0.5), 0)
        self.border_sprite = Sprite(self.pos.x, self.pos.y, f"caves/cave_BORDER", self.scale, self.angle)
        self.tint = (255, 255, 255, 255)
        self.angle = tile.angle
        self.tile_type = tile_type
        self.next_tile = tile_id

    def draw(self, surface: Surface) -> None:
        """
        Author: Yash Mahmud (32945795)

        Draws the cave sprite and its border on the provided surface.

        Parameters
        ----------
        surface : Surface
            The pygame surface where the cave will be drawn.
        """
        self.border_sprite.draw(surface)
        super().draw(surface)

    def set_tint(self, tint):
        """
        Author: Yash Mahmud (32945795)

        Applies a tint to the cave sprite to alter its appearance.

        Parameters
        ----------
        tint : tuple
            A tuple representing the RGBA color to tint the cave sprite.
        """
        self.tint = tint
        self.border_sprite.image.fill(self.tint, special_flags=BLEND_RGBA_MULT)

    def get_tile_type(self):
        """
        Author: Yash Mahmud (32945795)

        Returns the animal type associated with this cave.

        Returns
        -------
        AnimalType
            The animal type of the cave.
        """
        return self.tile_type

    def cave_next_tile(self):
        """
        Author: Yash Mahmud (32945795)

        Retrieves the ID of the next linked tile.

        Returns
        -------
        int
            The ID of the next linked tile.
        """
        return self.next_tile

    def save(self, data):
        """
        Author: Yash Mahmud (32945795)

        Saves the state of the cave to a dictionary.

        Parameters
        ----------
        data : dict
            The dictionary to save the cave's data into.
        """
        cave_data = {
            "cave_type": self.tile_type.name,
            "next_tile": self.next_tile,
            "cave_tint": self.tint
        }

        data["cave"] = cave_data

    def load(self, data):
        """
        Author: Yash Mahmud (32945795)

        Loads the cave's state from a dictionary.

        Parameters
        ----------
        data : dict
            The dictionary containing the cave's data.
        """
        self.tile_type = AnimalType[data["cave_type"]]
        self.next_tile = data["next_tile"]

        temp_angle = self.angle
        self.angle = 0
        self.set_sprite(f"caves/cave_{self.tile_type.name}")
        self.angle = temp_angle
        self.set_tint(data["cave_tint"])
