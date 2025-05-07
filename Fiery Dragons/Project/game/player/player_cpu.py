import random

from game.player.opponent_memory import OpponentMemory
from game.player.player import Player
from game.tile import Tile
from game.enums.playertypes import PlayerTypes


class PlayerCPU(Player):
    """
    Author: Anas Tarek Qumhiyeh (32985754)

    Represents a computer-controlled player, which simulates decision-making in the game.

    ...

    Attributes
    ----------
    board : Board
        The game board on which the CPU player operates.
    origin : Vector2
        The starting position of the CPU player on the board.
    start_tile : Tile
        The starting tile of the CPU player.
    player_id : int
        The unique identifier for the CPU player.
    turn_timer : int
        Countdown until the CPU player makes a move. Resets each turn.
    memory : dict
        A dictionary to store memory of opponent's moves, improving CPU strategy.

    Methods
    -------
    update():
        Manages the countdown timer and initiates the CPU's turn when the timer reaches zero.
    play_turn():
        Executes the CPU's move by flipping a chit card based on memory or randomly.
    guess(chit_cards):
        Decides which chit card to flip, using a memory system if available.
    add_to_memory(chit_card, difficulty):
        Adds a chit card to memory, considering game difficulty to influence memory retention.
    """
    def __init__(self, board, origin, start_tile: Tile, player_id: int):
        """
        Author: Anas Tarek Qumhiyeh (32985754)
        
        Constructs all the necessary attributes for the CPU player object.

        Parameters
        ----------
        board : Board
            The game board that the CPU player interacts with.
        origin : Vector2
            The physical origin point of the player on the game board.
        start_tile : Tile
            The starting tile where the CPU player begins the game.
        player_id : int
            The unique identifier for the CPU player.
        """
        super().__init__(board, origin, start_tile, player_id, PlayerTypes.CPU)
        self.turn_timer = 60
        self.memory = {}

    def update(self) -> None:
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Updates the internal state of the CPU player, counting down the turn timer and initiating the play turn when it reaches zero.
        """
        super().update()
        if self.board.current_player == self and self.turn_timer > 0:
            self.turn_timer -= 1
        elif self.turn_timer == 0:
            self.play_turn()
            self.turn_timer = 60

    def play_turn(self):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Handles the logic for the CPU player's turn, selecting and flipping a chit card.
        """
        chit_cards = self.board.tokens

        picked_card = self.guess(chit_cards)
        if not picked_card.flipped:
            picked_card.flip_token()

    def guess(self, chit_cards):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Uses either remembered information or random selection to choose a chit card to flip.

        Parameters
        ----------
        chit_cards : list
            List of all chit cards available on the board.

        Returns
        -------
        ChitCard
            The selected chit card to attempt to flip.
        """
        if self.get_is_in_cave():
            current_tile_type = self.currentTile.get_cave().get_tile_type()
        else:
            current_tile_type = self.currentTile.get_tile_type()

        cards_to_delete = []

        for key, val in self.memory.items():
            if val.forget():
                del val
                cards_to_delete.append(key)

        for card in cards_to_delete:
            self.memory.pop(card)

        for i in range(3):
            if "{0}_{1}".format(current_tile_type.name, str(i)) in self.memory:
                memory_data = self.memory["{0}_{1}".format(current_tile_type.name, str(i))]
                memory = memory_data.remember()

                if memory.flipped:
                    continue
                else:
                    return memory

        while True:
            memory = random.choice(chit_cards)
            if not memory.flipped:
                return memory

    def add_to_memory(self, chit_card, difficulty):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Adds a chit card to the CPU's memory based on the game's difficulty, affecting memory retention.

        Parameters
        ----------
        chit_card : ChitCard
            The chit card to remember.
        difficulty : DifficultyType
            The current difficulty setting of the game.
        """
        random_check, diff_range = difficulty.value

        if random.randint(0, 100) > random_check:
            return

        diff_min, diff_max = diff_range

        key = "{0}_{1}".format(chit_card.chit_type.name, str(chit_card.count))
        if key not in self.memory:
            self.memory[key] = OpponentMemory(chit_card, random.randint(diff_min, diff_max))
