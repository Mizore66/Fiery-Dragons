from game.player.player import Player
from game.tile import Tile
from game.enums.playertypes import PlayerTypes


class PlayerHuman(Player):
    """
    Author: Yash Mahmud (32945795)

    A class used to represent a human player, which is a subclass of Player.

    It has the same attributes as the Player class, but with a different player type.
    """
    def __init__(self, board, origin, start_tile: Tile, player_id: int):
        """
        Author: Yash Mahmud (32945795)

        Constructs all the necessary attributes for the human player object.

        Parameters
        ----------
            board : Board
                The board on which the player is placed.
            origin : Vector2
                The origin of the player.
            start_tile : Tile
                The starting position of the player.
            player_id : int
                The id of the player.
        """
        super().__init__(board, origin, start_tile, player_id, PlayerTypes.HUMAN)
