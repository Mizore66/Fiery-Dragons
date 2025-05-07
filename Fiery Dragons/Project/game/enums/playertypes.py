from enum import Enum


class PlayerTypes(Enum):
    """
    Author: Anas Tarek Qumhiyeh (32985754)
    
    An enumeration to distinguish between different types of players in the game.

    Attributes
    ----------
    HUMAN : int
        Represents a human player, typically interacting through a user interface.
    CPU : int
        Represents a computer-controlled player, operating through predefined algorithms.
    """
    HUMAN = 0
    CPU = 1