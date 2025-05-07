from abc import abstractmethod


class State:
    """
    An abstract class representing the state of an object.

    Author: Yash Mahmud (32945795)

    Methods
    -------
    save(data):
        Abstract method to save the state of an object.
    load(data):
        Abstract method to load the state of an object.
    """

    @abstractmethod
    def save(self, data):
        """
        Author: Yash Mahmud (32945795)

        Abstract method to save the state of an object.

        Parameters
        ----------
            data : dict
                The dictionary to save the state of the object into.
        """
        pass

    @abstractmethod
    def load(self, data):
        """
        Author: Yash Mahmud (32945795)

        Abstract method to load the state of an object.

        Parameters
        ----------
            data : dict
                The dictionary to load the state of the object from.
        """
        pass
