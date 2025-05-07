from abc import ABC

from engine.state import State


class VolcanoCard(State, ABC):
    """
    Author: Chua Xian Loong (32669747)

    Represents a collection of tiles grouped as a "Volcano Card" in the game. This class provides the structure
    to manage the operations related to a set of tiles that form a part of the game board's layout.

    Attributes
    ----------
    id : int
        A unique identifier for the Volcano Card.
    animals : tuple
        A tuple containing Tile objects that are part of the Volcano Card.

    Methods
    -------
    __init__(*animals):
        Initializes a new instance of VolcanoCard with a specified set of tiles.
    __iter__():
        Returns an iterator for the tiles in the Volcano Card.
    __getitem__(item):
        Allows direct access to a specific tile in the Volcano Card by index.
    __len__():
        Returns the number of tiles in the Volcano Card.
    get_id() -> int:
        Retrieves the identifier of the Volcano Card.
    set_id(volcano_id: int):
        Sets the identifier for the Volcano Card.
    draw(surface: Surface):
        Draws all the tiles in the Volcano Card onto a given surface.
    save(data: dict):
        Saves the state of the Volcano Card to a dictionary object for serialization.
    load(data: dict):
        Loads the state of the Volcano Card from a dictionary object.
    """

    def __init__(self, *animals):
        """
        Author: Chua Xian Loong (32669747)

        Initializes the VolcanoCard with the specified tiles.

        Parameters
        ----------
        animals : tuple
            A variable number of Tile objects that make up the Volcano Card.
        """
        self.id = 0
        self.animals = animals

    def __iter__(self):
        """
        Author: Chua Xian Loong (32669747)

        Returns an iterator for the tiles in the Volcano Card.

        Returns
        -------
        iter
            An iterator for the tiles in the Volcano Card.
        """
        return iter(self.animals)

    def __getitem__(self, item):
        """
        Author: Chua Xian Loong (32669747)

        Allows direct access to a specific tile in the Volcano Card by index.

        Parameters
        ----------
        item : int
            The index of the tile to retrieve.
        """
        return self.animals[item]

    def __len__(self):
        """
        Author: Chua Xian Loong (32669747)

        Returns the number of tiles in the Volcano Card.

        Returns
        -------
        int
            The number of tiles in the Volcano Card.
        """
        return len(self.animals)

    def get_id(self):
        """
        Author: Chua Xian Loong (32669747)

        Retrieves the identifier of the Volcano Card.

        Returns
        -------
        int
            The unique identifier of the Volcano Card.
        """
        return self.id

    def set_id(self, volcano_id):
        """
        Author: Chua Xian Loong (32669747)

        Sets the identifier for the Volcano Card.

        Parameters
        ----------
        volcano_id : int
            The new identifier for the Volcano Card.
        """
        self.id = volcano_id

    def draw(self, surface):
        """
        Author: Chua Xian Loong (32669747)

        Draws each tile in the Volcano Card on the specified drawing surface.

        Parameters
        ----------
        surface : Surface
            The Pygame surface on which to draw the tiles.
        """
        for tile in self.animals:
            tile.draw(surface)

    def save(self, data):
        """
        Author: Chua Xian Loong (32669747)

        Saves the state of the Volcano Card to a dictionary, allowing it to be serialized.

        Parameters
        ----------
        data : dict
            The dictionary to which the Volcano Card's state will be saved.
        """
        volcano_data = {}
        for i, tile in enumerate(self.animals):
            volcano_data["tile_" + str(i)] = tile.save(volcano_data)

        data['volcano_' + str(self.id)] = volcano_data

    def load(self, data):
        """
        Author: Chua Xian Loong (32669747)
        
        Loads the Volcano Card's state from the given dictionary.

        Parameters
        ----------
        data : dict
            The dictionary from which to load the Volcano Card's state.
        """
        volcano_data = data['volcano_' + str(self.id)]
        for i, tile in enumerate(self.animals):
            tile.load(volcano_data["tile_" + str(i)])
