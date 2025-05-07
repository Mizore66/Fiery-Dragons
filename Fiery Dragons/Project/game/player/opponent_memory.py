class OpponentMemory:
    """
    Author: Anas Tarek Qumhiyeh (32985754)

    A class used to represent the memory of a CPU player regarding chit cards in the game.

    ...

    Attributes
    ----------
    chit_card : ChitCard
        The chit card remembered by the CPU player.
    timer : int
        A countdown timer that determines how long the memory of the chit card lasts.

    Methods
    -------
    get_chit_card():
        Returns the chit card stored in memory.
    remember():
        Decrements the memory timer and returns the chit card if still remembered.
    forget():
        Decrements the memory timer and checks if the memory should be forgotten.
    has_forgotten():
        Checks if the timer has elapsed and the memory is lost.
    """

    def __init__(self, chit_card, timer):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Constructs all the necessary attributes for the OpponentMemory object.

        Parameters
        ----------
        chit_card : ChitCard
            The chit card to be remembered.
        timer : int
            The duration (in turns or some other unit of time) for which this memory is valid.
        """
        self.chit_card = chit_card
        self.timer = timer

    def get_chit_card(self):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Returns the chit card stored in memory.

        Returns
        -------
        ChitCard
            The chit card remembered by the CPU player.
        """
        return self.chit_card

    def remember(self):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Decrements the memory timer each call, representing the passing of time.

        Returns
        -------
        ChitCard
            The chit card if it is still within the memory timer.
        """
        self.timer -= 1
        return self.chit_card

    def forget(self):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Decrements the memory timer and checks if the memory should be forgotten.

        Returns
        -------
        bool
            True if the timer has reached zero and the memory should be discarded, False otherwise.
        """
        self.timer -= 1
        return self.timer <= 0

    def has_forgotten(self):
        """
        Author: Anas Tarek Qumhiyeh (32985754)
        
        Checks if the memory timer has expired.

        Returns
        -------
        bool
            True if the memory is no longer valid, False otherwise.
        """
        return self.timer <= 0