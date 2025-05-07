import json
import random

from math import floor, ceil, inf
from pygame import Vector2, Surface, Color

from game.dragon import Dragon
from game.enums.difficultytypes import DifficultyType
from game.enums.playertypes import PlayerTypes
from game.volcanoCard import VolcanoCard
from engine.text import Text
from engine.utils import lengthdir_x, lengthdir_y
from game.player.player import Player
from game.player.player_human import PlayerHuman
from game.player.player_cpu import PlayerCPU
from game.tile import Tile
from game.enums.animaltypes import AnimalType

from game.chitcards.chit_bat import ChitBat
from game.chitcards.chit_egg import ChitEgg
from game.chitcards.chit_pirate import ChitPirate
from game.chitcards.chit_salamander import ChitSalamander
from game.chitcards.chit_spider import ChitSpider
from game.chitcards.chit_knight import ChitKnight


class Board:
    """
    Author: Yash Mahmud (32945795)

    A class used to represent a Board.

    ...

    Attributes
    ----------
    players : list
        A list of players in the game.
    tiles : list
        A list of tiles on the board.
    tokens : list
        A list of tokens on the board.
    origin : Vector2
        The origin of the board.
    current_player : Player
        The current player.
    winner : Player
        The winner of the game.
    current_player_text : Text
        The text displaying the current player's turn.

    Methods
    -------
    __init__(pos, difficulty, cpu_count):
        Constructs all the necessary attributes for the board object.
    winner_check() -> Player | bool:
        Checks if there is a winner.
    draw(surface: Surface) -> None:
        Draws the board on the given surface.
    update() -> None:
        Updates the state of the board.
    get_tile(tile_id: int) -> Tile:
        Returns the tile with the given id.
    add_player(player: Player) -> None:
        Adds a player to the board.
    swap_player():
        Swaps the current player with the nearest player that is not in a cave.
    move_player(turns: int, chit_type: AnimalType) -> bool:
        Moves the current player.
    switch_player() -> None:
        Switches the current player.
    save(filename='savedata.json'):
        Saves the current state of the board to a JSON file.
    load(filename):
        Loads the saved state of the board from a JSON file.

    """

    def __init__(self, pos: Vector2, difficulty, cpu_count):
        """
        Author: Yash Mahmud (32945795)

        Constructs all the necessary attributes for the board object.

        Parameters
        ----------
        pos : Vector2
            A tuple representing the position of the board (x, y).
        difficulty : DifficultyType
            The difficulty level of the game.
        cpu_count : int
            The number of CPU players in the game.
        """

        self.VOLCANO_COUNT = 8
        self.player_order = [1, 2, 3, 4]
        self.window_open = False

        self.finished = False
        volcano_cards_data = [
            [AnimalType.EGG, AnimalType.BAT, AnimalType.SPIDER],
            [AnimalType.SALAMANDER, AnimalType.SPIDER, AnimalType.BAT],
            [AnimalType.SPIDER, AnimalType.SALAMANDER, AnimalType.EGG],
            [AnimalType.BAT, AnimalType.SPIDER, AnimalType.EGG],
            [AnimalType.SPIDER, AnimalType.BAT, AnimalType.SALAMANDER],
            [AnimalType.EGG, AnimalType.SALAMANDER, AnimalType.BAT],
            [AnimalType.BAT, AnimalType.EGG, AnimalType.SALAMANDER],
            [AnimalType.SALAMANDER, AnimalType.EGG, AnimalType.SPIDER]
        ]

        tile_count = sum(len(card) for card in volcano_cards_data)

        if self.VOLCANO_COUNT > 8:
            for i in range(ceil(tile_count - 24 / 3)):
                volcano_cards_data.append(random.choice(volcano_cards_data))

        # Randomize volcano cards
        random.shuffle(volcano_cards_data)

        # Initial cave types
        caves = [AnimalType.BAT,
                 AnimalType.SPIDER,
                 AnimalType.EGG,
                 AnimalType.SALAMANDER]

        # Randomize caves
        random.shuffle(caves)

        self.tokens = []
        self.origin = pos

        self.current_player = None
        self.winner = None
        self.difficulty = difficulty
        self.cpu_count = cpu_count
        self.cave_positions = [0, 6, 12, 18]

        self.create_board(volcano_cards_data, caves)

        # Hardcoded token positions
        token_pos = [
            [-82, -103],
            [49, -128],
            [-12, -139],
            [97, -72],
            [-69, -42],
            [6, -54],
            [-126, 9],
            [48, 3],
            [128, 10],
            [-97, 90],
            [-59, 34],
            [-36, 113],
            [9, 60],
            [70, 54],
            [108, 105],
            [34, 133],
            [-120, -48]
        ]

        for i in range(len(token_pos)):
            token_pos[i] = [x + random.randint(-2, 2) for x in token_pos[i]]

        random.shuffle(token_pos)

        # Hardcoded token objects
        self.tokens = [
            ChitBat(self.origin[0] + token_pos[0][0], self.origin[1] + token_pos[0][1], (0.45, 0.45), self, 3, 0),
            ChitEgg(self.origin[0] + token_pos[1][0], self.origin[1] + token_pos[1][1], (0.45, 0.45), self, 1, 1),
            ChitSpider(self.origin[0] + token_pos[2][0], self.origin[1] + token_pos[2][1], (0.45, 0.45), self, 1, 2),
            ChitPirate(self.origin[0] + token_pos[3][0], self.origin[1] + token_pos[3][1], (0.45, 0.45), self, 2, 3),
            ChitPirate(self.origin[0] + token_pos[4][0], self.origin[1] + token_pos[4][1], (0.45, 0.45), self, 1, 4),
            ChitBat(self.origin[0] + token_pos[5][0], self.origin[1] + token_pos[5][1], (0.45, 0.45), self, 2, 5),
            ChitSalamander(self.origin[0] + token_pos[6][0], self.origin[1] + token_pos[6][1], (0.45, 0.45), self, 1,
                           6),
            ChitBat(self.origin[0] + token_pos[7][0], self.origin[1] + token_pos[7][1], (0.45, 0.45), self, 1, 7),
            ChitPirate(self.origin[0] + token_pos[8][0], self.origin[1] + token_pos[8][1], (0.45, 0.45), self, 2, 8),
            ChitSalamander(self.origin[0] + token_pos[9][0], self.origin[1] + token_pos[9][1], (0.45, 0.45), self, 2,
                           9),
            ChitEgg(self.origin[0] + token_pos[10][0], self.origin[1] + token_pos[10][1], (0.45, 0.45), self, 2, 10),
            ChitSalamander(self.origin[0] + token_pos[11][0], self.origin[1] + token_pos[11][1], (0.45, 0.45), self, 3,
                           11),
            ChitEgg(self.origin[0] + token_pos[12][0], self.origin[1] + token_pos[12][1], (0.45, 0.45), self, 3, 12),
            ChitSpider(self.origin[0] + token_pos[13][0], self.origin[1] + token_pos[13][1], (0.45, 0.45), self, 3, 13),
            ChitSpider(self.origin[0] + token_pos[14][0], self.origin[1] + token_pos[14][1], (0.45, 0.45), self, 2, 14),
            ChitPirate(self.origin[0] + token_pos[15][0], self.origin[1] + token_pos[15][1], (0.45, 0.45), self, 1, 15),
            ChitKnight(self.origin[0] + token_pos[16][0], self.origin[1] + token_pos[16][1], (0.45, 0.45), self, 1, 16),
        ]

        self.init_players(self.cpu_count)

        # Initialize current turn text
        self.current_player_text = Text("{0}'s turn".format(self.current_player), Vector2(20, 20), Color(255, 255, 255),
                                        "calist")
        
        self.dragon = Dragon(self)

    def create_board(self, volcano_cards_data, caves):
        """
        Author: Yash Mahmud (32945795)

        Initializes the board layout by placing tiles and cave positions based on the specified volcano card data and cave types.

        Parameters
        ----------
        volcano_cards_data : list[list[AnimalType]]
            A list containing the distribution of AnimalTypes for each volcano card, determining the tile arrangement on the board.
        caves : list[AnimalType]
            A list of AnimalTypes specifying the types of caves at predefined positions on the board.
        """
        self.volcano_cards = []

        cave_counter = 0
        i = 0

        self.VOLCANO_COUNT = len(volcano_cards_data)

        tile_count = sum(len(card) for card in volcano_cards_data)

        print(self.VOLCANO_COUNT, tile_count)

        for card in volcano_cards_data:
            current_volcano_card = []
            for tile in card:
                angle = (-360 * (i / tile_count)) + 180
                scale_factor = 0.01
                scale = (0.5 - (scale_factor * (tile_count - 24)), 0.5 - (scale_factor * (tile_count - 24)))

                dist = 460 * scale[0] + (6 * (tile_count - 24))

                pos = Vector2(lengthdir_x(dist, angle), lengthdir_y(dist, angle))
                player_pos = Vector2(self.origin[0] + lengthdir_x(dist + 640 * scale[0], angle),
                                     self.origin[1] + lengthdir_y(dist + 640 * scale[0], angle))

                if i in self.cave_positions and cave_counter < 4:
                    current_tile = Tile(self.origin[0] + pos[0], self.origin[1] + pos[1], tile, i, scale, angle,
                                        player_pos,
                                        True,
                                        caves[cave_counter])
                    cave_counter += 1
                else:
                    current_tile = Tile(self.origin[0] + pos[0], self.origin[1] + pos[1], tile, i, scale, angle,
                                        player_pos)

                i += 1
                current_volcano_card.append(current_tile)

            volc_card = VolcanoCard(*current_volcano_card)
            volc_card.set_id(len(self.volcano_cards))
            self.volcano_cards.append(volc_card)

    def init_players(self, cpu_count):
        """
        Author: Yash Mahmud (32945795)

        Initializes the players on the board, adding human and CPU players based on the specified CPU count.

        Parameters
        ----------
        cpu_count : int
            The number of CPU players to add to the board.
        """
        self.players: list[Player] = []

        # Add all players to the board
        human_count = 4 - cpu_count
        for i in range(human_count):
            self.add_player(PlayerHuman(self, self.origin, self.get_tile(self.cave_positions[i]), i))
        for i in range(human_count, 4):
            self.add_player(PlayerCPU(self, self.origin, self.get_tile(self.cave_positions[i]), i))

    def winner_check(self) -> Player | bool:
        """
        Author: Yash Mahmud (32945795)

        Checks if there is a winner.

        Returns
        -------
            Player or bool
                The winner of the game if there is one, False otherwise.
        """
        if self.winner is not None:
            self.finished = True
            return self.winner
        else:
            return False

    def draw(self, surface: Surface) -> None:
        """
        Author: Yash Mahmud (32945795)

        Draws the board on the given surface.

        Parameters
        ----------
            surface : Surface
                the surface to draw the board on
        """
        for spr in self.volcano_cards + self.tokens + self.players:
            spr.draw(surface)

        self.current_player_text.draw(surface)

    def update(self) -> None:
        """
        Author: Yash Mahmud (32945795)

        Updates the state of the board.
        """
        for player in self.players:
            player.update()

        if self.get_finished():
            return

        for token in self.tokens:
            token.update()

    def get_tile(self, tile_id: int) -> Tile:
        """
        Author: Yash Mahmud (32945795)

        Returns the tile with the given id.

        Parameters
        ----------
            tile_id : int
                the id of the tile

        Returns
        -------
            Tile
                the tile with the given id
        """
        for card in self.volcano_cards:
            for tile in card:
                if tile.get_tile_id() == tile_id:
                    return tile

    def __len__(self):
        """
        Author: Yash Mahmud (32945795)
        
        Returns the number of tiles on the board.

        Returns
        -------
            int
                the number of tiles on the board
        """
        return sum(len(card) for card in self.volcano_cards)

    def get_cave_tiles(self):
        """
        Author: Yash Mahmud (32945795)

        Returns the IDs of all cave tiles on the board.

        Returns
        -------
            list[int]
                a list of tile IDs for all cave tiles on the board
        """
        cave_tiles = []
        for card in self.volcano_cards:
            for tile in card:
                if tile.get_cave():
                    cave_tiles.append(tile.get_tile_id())

        return cave_tiles

    def add_player(self, player: Player) -> None:
        """
        Author: Yash Mahmud (32945795)

        Adds a player to the board.

        Parameters
        ----------
            player : Player
                the player to be added
        """
        self.players.append(player)

        if self.current_player is None:
            self.current_player = player

    def swap_player(self):
        """
        Author: Aditti Gupta (32863357)

        Swaps the current player with the nearest player that is not in a cave.
        """
        self.dragon.swap()


    def move_player(self, turns: int, chit_type: AnimalType) -> bool:
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Moves the current player.

        Parameters
        ----------
            turns : int
                the number of turns to move
            chit_type : AnimalType
                the type of the chit

        Returns
        -------
            bool
                whether the player gets another turn or not

        """

        return self.dragon.move(turns, chit_type)

    def add_to_memories(self, token):
        """
        Author: Yash Mahmud (32945795)

        Adds the token to the memory of the current player.

        Parameters
        ----------
        token : ChitCard
            the token to be added to the memory
        """
        for player in self.players:
            if player.player_type == PlayerTypes.CPU:
                player.add_to_memory(token, self.difficulty)

    def switch_player(self) -> None:
        """
        Author: Anas Tarek Qumhiyeh (32985754)
        
        Switches the current player.
        """
        self.dragon.switch()

    def get_finished(self) -> bool:
        """
        Author: Yash Mahmud (32945795)

        Returns whether the game has finished.

        Returns
        -------
            bool
                True if the game has finished, False otherwise
        """
        return self.finished

    def save(self, filename='savedata.json'):
        """
        Author: Yash Mahmud (32945795)

        Saves the current game state including player positions, token states, and other relevant data to a JSON file.

        Parameters
        ----------
        filename : str
            The name of the file where the game state will be saved.
        """
        data = {}

        game_data = {
            'current_player': self.current_player.player_id,
            'difficulty': self.difficulty.name,
            'cpu_count': self.cpu_count,
            'player_order': self.player_order
        }

        data['game'] = game_data
        data['volcanoes'] = {}

        for objects in self.volcano_cards:
            objects.save(data['volcanoes'])

        for objects in self.tokens + self.players:
            objects.save(data)

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load(self, filename):
        """
        Author: Yash Mahmud (32945795)

        Loads a game state from a specified JSON file into the board, reconstructing the player positions, token states, and other game data.

        Parameters
        ----------
        filename : str
            The name of the file from which the game state is to be loaded.
        """
        with open(filename, 'r') as file:
            data = json.load(file)

        game_data = data['game']
        self.current_player = self.players[game_data['current_player']]
        self.current_player_text.set_text("{0}'s turn".format(self.current_player))
        self.difficulty = DifficultyType[game_data['difficulty']]
        self.cpu_count = game_data['cpu_count']
        self.player_order = game_data['player_order']

        v_data = data['volcanoes']

        volcano_cards_data = []

        self.cave_positions = []

        i = 0
        for key, value in v_data.items():
            temp_vcard = []

            for key2, value2 in value.items():
                temp_vcard.append(AnimalType[value2['tileType']])
                if 'cave' in value2:
                    self.cave_positions.append(i)
                i += 1

            volcano_cards_data.append(temp_vcard)

        print(self.cave_positions)

        caves = [AnimalType.BAT,
                 AnimalType.SPIDER,
                 AnimalType.EGG,
                 AnimalType.SALAMANDER]

        self.create_board(volcano_cards_data, caves)
        self.init_players(self.cpu_count)

        for objects in self.volcano_cards:
            objects.load(v_data)

        for objects in self.tokens + self.players:
            objects.load(data)
