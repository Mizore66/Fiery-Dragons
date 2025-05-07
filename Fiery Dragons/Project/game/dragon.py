from math import inf

from game.enums.animaltypes import AnimalType
from game.tile import Tile
from game.player.player import Player


class Dragon:
    """
    Author: Anas Tarek Qumhiyeh (32985754)

    Manages the player movement and interactions on the board based on various game rules and mechanics such as cave interactions and chit card influences.

    Attributes
    ----------
    board : Board
        The board on which the Dragon is operating, facilitating access to other game components.

    Methods
    -------
    move(turns: int, chit_type: AnimalType) -> bool:
        Attempts to move the current player based on the chit drawn and the player's current position.
    swap():
        Swaps the current player with another player not in a cave, based on the closest distance.
    switch():
        Cycles to the next player in the game order, updating game state accordingly.
    """
    def __init__(self, board):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Initializes a Dragon with a reference to the board.

        Parameters
        ----------
        board : Board
            The game board that the Dragon will interact with.
        """
        self.board = board

    def move(self, turns: int, chit_type: AnimalType) -> bool:
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Moves the current player based on the drawn chit type and the number of turns specified. Determines whether the player can move or if the turn ends based on the game's rules.

        Parameters
        ----------
        turns : int
            The number of spaces the player should move.
        chit_type : AnimalType
            The type of chit drawn that determines the movement rules.

        Returns
        -------
        bool
            True if the player can continue playing (e.g., drawing another chit), False if their turn ends.
        """

        # This condition checks if the player is still in their cave 
        if self.board.current_player.get_is_in_cave():
            # Grabs the animal type of the cave the player is in and compare to the chit card
            if self.board.current_player.get_tile().cave.tile_type == chit_type:
                tile_id = (self.board.current_player.get_cave().next_tile + turns - 1) % len(self.board)
                new_tile = self.board.get_tile(tile_id)

                if new_tile.is_occupied():
                    self.board.switch_player()
                    return False
                
                self.board.current_player.move(turns)
                return True
            elif chit_type == AnimalType.PIRATE:
                return True
            else:
                self.board.switch_player()
                return False

        # This condition checks if the chit type matches the current tile type. If it does, the player is moved.
        elif self.board.current_player.get_tile().get_tile_type() == chit_type or chit_type == AnimalType.PIRATE:
            tile_id = self.board.current_player.get_tile().get_tile_id()
            new_tile = self.board.get_tile((tile_id + turns) % len(self.board))

            if new_tile.is_occupied():
                self.board.switch_player()
                return False
            
            self.board.current_player.move(turns)
            return True

        # If none of the above conditions are met, the current player is switched and an effect is applied if possible.
        else:
            # This condition checks if the current chit type is KNIGHT.
            if chit_type == AnimalType.KNIGHT:
                self.board.swap_player()

            self.board.switch_player()
            return False
    
    def swap(self):
        """
        Author: Aditti Gupta (32863357)

        Swaps the current player with the closest player not currently in a cave, taking into account the topology of the board and player positions.

        This method recalculates the optimal path for swapping and updates player positions accordingly.
        """
        min_diff = inf

        nearest_player: Player = self.board.current_player
        my_player: Player = self.board.current_player

        forward_diff, backward_diff = 0, 0

        for player_index in range(len(self.board.players)):
            temp_player: Player = self.board.players[player_index]

            if temp_player.player_id != my_player.player_id:
                if not temp_player.get_is_in_cave():
                    player_pos = temp_player.get_tile().get_tile_id()
                    my_player_pos = my_player.get_tile().get_tile_id()

                    forward_diff = (player_pos - my_player_pos) % len(self.board)
                    backward_diff = (my_player_pos - player_pos) % len(self.board)

                    min_diff_index_player = min(forward_diff, backward_diff)

                    if min_diff_index_player < min_diff:
                        min_diff = min_diff_index_player
                        nearest_player = temp_player

        my_player_tile: Tile = my_player.currentTile
        nearest_player_tile: Tile = nearest_player.currentTile
        temp_tile: Tile = my_player_tile

        my_player_tile = nearest_player_tile
        my_player_tile.occupant = my_player

        nearest_player_tile = temp_tile
        nearest_player_tile.occupant = nearest_player

        if min_diff == forward_diff:
            my_player.steps += min_diff
            nearest_player.steps -= min_diff
        else:
            my_player.steps -= min_diff
            nearest_player.steps += min_diff

        my_player.move_to_tile(my_player_tile)
        nearest_player.move_to_tile(nearest_player_tile)
        my_player.currentTile.occupant = my_player
        nearest_player.currentTile.occupant = nearest_player
    
    def switch(self) -> None:
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Switches the focus to the next player in the predefined player order, ensuring the game cycle continues smoothly.

        This method updates the game state to reflect the change in active player and handles any necessary updates to game tokens or effects.
        """
        current_index = self.board.player_order.index(self.board.current_player.player_id + 1) % 4
        player_id = self.board.player_order[(current_index + 1) % 4] - 1

        self.board.current_player = self.board.players[player_id]
        self.board.current_player_text.set_text("{0}'s turn".format(self.board.current_player))

        # Fix it so that tokens that are still flipping are not affected
        for token in self.board.tokens:
            if token.flipped and not token.flip_animation.is_playing():
                token.flip_animation.play_animation()