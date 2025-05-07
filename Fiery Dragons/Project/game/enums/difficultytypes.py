from enum import Enum


class DifficultyType(Enum):
    """
    Author: Anas Tarek Qumhiyeh (32985754)

    An enumeration class for the different types of difficulties.

    Attributes
    ----------
    EASY : tuple
        Represents the easy difficulty type.
    MEDIUM : tuple
        Represents the medium difficulty type.
    HARD : tuple
        Represents the hard difficulty type.
    """
    EASY = (80, (1, 3))
    MEDIUM = (90, (2, 5))
    HARD = (99, (3, 9))
