from abc import ABC

from pygame import Surface, Vector2

from engine.sprite import Sprite
from engine.state import State
from game.cave import Cave
from game.enums.animaltypes import AnimalType


class Tile(Sprite, State, ABC):
    """
    Author: Yash Mahmud (32945795)

    Represents a Tile in the game board, which can contain various game elements such as caves or occupants (players).

    Attributes
    ----------
    tileType : AnimalType
        The type of animal associated with the tile.
    tileId : int
        The unique identifier for the tile.
    player_pos : Vector2
        The position on the screen where the player token will be drawn if they occupy this tile.
    occupant : Player or None
        Reference to the Player object that is currently occupying the tile, None if the tile is unoccupied.
    tileSpr : Sprite
        The visual representation of the tile.
    cave : Cave or None
        An optional Cave object if the tile represents a cave entrance.

    Methods
    -------
    draw(surface: Surface):
        Draws the tile and its contents (e.g., cave, occupant) onto the given surface.
    get_tile_id() -> int:
        Returns the unique identifier of the tile.
    get_tile_type() -> AnimalType:
        Retrieves the animal type associated with the tile.
    get_cave() -> Cave or None:
        Returns the cave object associated with the tile, if it exists.
    is_occupied() -> bool:
        Checks if the tile is currently occupied by a player.
    save():
        Saves the state of the tile to a dictionary object.
    load(data: dict):
        Loads the state of the tile from a dictionary object.
    """

    def __init__(self, x: int, y: int, tile_type: AnimalType, tile_id: int, scale: tuple, angle: int,
                 player_pos: Vector2, has_cave: bool = False, cave_type: AnimalType = None):
        """
        Initializes a Tile with location, type, and optional cave features.

        Parameters
        ----------
        x : int
            X-coordinate of the tile.
        y : int
            Y-coordinate of the tile.
        tile_type : AnimalType
            The type of animal associated with the tile.
        tile_id : int
            The unique identifier for the tile.
        scale : tuple
            Scaling factors for the tile dimensions.
        angle : int
            Rotation angle of the tile sprite.
        player_pos : Vector2
            The screen coordinates for placing a player token.
        has_cave : bool, optional
            Indicates whether this tile should include a cave.
        cave_type : AnimalType, optional
            The type of animal associated with the cave, if one is included.
        """
        super().__init__(x, y, "sprTile", scale, angle)

        self.tileType = tile_type
        self.tileId = tile_id

        self.player_pos = player_pos

        self.cave = Cave(cave_type, self, tile_id) if has_cave else None
        self.occupant = None

        tile_spr = "tiles/{0}".format(tile_type.name.lower())

        self.tileSpr = Sprite(x, y, tile_spr, (scale[0] * 0.2, scale[1] * 0.2), 0)

    def draw(self, surface: Surface) -> None:
        """
        Draws the tile on the given surface.

        Parameters
        ----------
            surface : Surface
                the surface to draw the tile on
        """
        super().draw(surface)
        self.tileSpr.draw(surface)
        if self.cave:
            self.cave.draw(surface)

    def get_tile_id(self) -> int:
        """
        Returns the id of the tile.

        Returns
        -------
            int
                the id of the tile
        """
        return self.tileId

    def get_tile_type(self) -> AnimalType:
        """
        Returns the type of the tile.

        Returns
        -------
            AnimalType
                the type of the tile
        """
        return self.tileType

    def get_cave(self) -> bool:
        """
        Returns the cave object associated with the tile. (if it exists)

        Returns
        -------
            Cave or None
                the cave object associated with the tile
        """
        return self.cave

    def is_occupied(self) -> bool:
        """
        Returns True if the tile is occupied, False otherwise.

        Returns
        -------
            bool
                True if the tile is occupied, False otherwise
        """
        return self.occupant is not None

    def save(self, data):
        """
        Author: Yash Mahmud (32945795)

        Saves the state of the Tile.
        """
        tile_data = {
            "tileType": self.tileType.name
        }

        if self.get_cave():
            self.get_cave().save(tile_data)

        return tile_data

    def load(self, data):
        """
        Author: Yash Mahmud (32945795)

        Loads the state of the Tile.

        Parameters
        ----------
            data : dict
                the dictionary containing the Tile state data
        """
        self.tileType = AnimalType[data['tileType']]
        self.tileSpr.set_sprite("tiles/{0}".format(self.tileType.name.lower()))

        if "cave" in data:
            self.cave = Cave(AnimalType.BAT, self, self.get_tile_id())
            self.get_cave().load(data["cave"])
        else:
            self.cave = None

