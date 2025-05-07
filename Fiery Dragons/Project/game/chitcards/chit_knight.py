from abc import ABC

from game.chitcards.token import Token
from game.enums.animaltypes import AnimalType


class ChitKnight(Token, ABC):
    """
    Author: Aditti Gupta (32863357) 

    A class used to represent a Pirate Knight Chit Card, which is a subclass of Token.

    It has the same attributes as the Token class, but with a different chit type.
    """

    def __init__(self, x: int, y: int, scale: tuple, board, count: int, token_id: int):
        """
        Author: Aditti Gupta (32863357)
        
        Constructs all the necessary attributes for the Pirate Knight Chit Card object.

        Parameters
        ----------
            x : int
                x-coordinate of the Chit Card
            y : int
                y-coordinate of the Chit Card
            scale : float
                the scale of the Chit Card
            board : Board
                the board on which the Chit Card is placed
            count : int
                the number of steps for the Chit Card
        """
        super().__init__(x, y, scale, board, count, AnimalType.KNIGHT, token_id)
