from abc import ABC

from pygame import Surface, Vector2

from engine.animation import Animation
from engine.button import Button
from engine.state import State
from game.enums.animaltypes import AnimalType
from engine.utils import play_sound
from game.enums.playertypes import PlayerTypes


class Token(Button, ABC, State):
    """
    Author: Yash Mahmud (32945795)

    A class used to represent a Token, which is a subclass of Button.

    ...

    Attributes
    ----------
    board : Board
        The board on which the Token is placed.
    click_timer : int
        A timer for the click event.
    count : int
        The number of steps for the Chit Card
    chit_type : AnimalType
        The type of the chit.
    flipped : bool
        Whether the chit card is flipped or not.
    token_id : int
        The id of the token.
    flip_animation : Animation
        The animation for flipping the chit card.

    Methods
    -------
    draw(surface):
        Draws the Token on the given surface.
    on_click():
        Defines what happens when the Token is clicked.
    flip_token():
        Flips the token.
    set_flip_sprite(show_front):
        Flips the chit_card of a position.
    save(data):
        Saves the state of the Token.
    load(data):
        Loads the state of the Token.
    """

    def __init__(self, x: int, y: int, scale: tuple, board, count: int, chit_type: AnimalType, token_id: int):
        """
        Author: Yash Mahmud (32945795)

    
        Constructs all the necessary attributes for the Token object.

        Parameters
        ----------
            x : int
                x-coordinate of the Token
            y : int
                y-coordinate of the Token
            scale : tuple
                the scale of the Token
            board : Board
                the board on which the Token is placed
            count : int
                the number of steps for the Token
            chit_type : AnimalType
                the type of the chit
        """
        super().__init__(x, y, "sprToken", scale)
        self.board = board
        self.click_timer = 0
        self.count = count
        self.chit_type = chit_type
        self.flipped = False
        self.token_id = token_id

        self.flip_animation = Animation([1, 0.8, 0.4, 0.2, 0, 0.2, 0.4, 0.8, 1], 1)

    def draw(self, surface: Surface) -> None:
        """
        Author: Yash Mahmud (32945795)

        Draws the Token on the given surface.

        Parameters
        ----------
            surface : Surface
                the surface to draw the Token on
        """
        super().draw(surface)

        if self.click_timer > 0:
            self.click_timer -= 1
            if self.click_timer == 0:
                self.flip_animation.play_animation()

        self.flip_animation.update()

        if self.flip_animation.is_playing():
            if self.flip_animation.get_current_frame() == 0:
                self.set_flip_sprite(not self.flipped)

            self.set_scale(0.45 * self.flip_animation.get_current_frame(), 0.45)

    def on_click(self) -> None:
        """
        Author: Yash Mahmud (32945795)

        Defines what happens when the Token is clicked.
        """
        if not self.flipped and self.board.current_player.player_type == PlayerTypes.HUMAN and not self.board.window_open:
            self.flip_token()

    def flip_token(self):
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Flips the token.
        """
        if not self.board.move_player(self.count, self.chit_type):
            self.click_timer = 30
        self.flip_animation.play_animation()
        self.board.add_to_memories(self)
        play_sound("sndCardFlip")

    def set_flip_sprite(self, show_front: bool) -> None:
        """
        Author: Anas Tarek Qumhiyeh (32985754)

        Function to flip the chit_card of a position

        Parameters
        ----------
            screen : Surface
                the screen to draw the chit_card on
            show_front : bool
                what side to flip the token

        """

        # Draw the image based on the flip_progress
        if show_front:
            self.set_sprite("chitcards/chit_{0}{1}".format(abs(self.count), self.chit_type.name.lower()))
        else:
            self.set_sprite("sprToken")
        self.flipped = show_front

    def save(self, data):
        """
        Author: Yash Mahmud (32945795)

        Saves the state of the Token.

        Parameters
        ----------
            data : dict
                the dictionary to save the Token state to
        """
        token_data = {
            'x': int(self.pos.x),
            'y': int(self.pos.y),
            'flipped': self.flipped,
            'chit_type': self.chit_type.name,
            'count': self.count
        }
        data['token_' + str(self.token_id)] = token_data

    def load(self, data):
        """
        Author: Yash Mahmud (32945795)

        Loads the state of the Token.

        Parameters
        ----------
            data : dict
                the dictionary to load the Token state from
        """
        token_data = data['token_' + str(self.token_id)]
        self.set_position(Vector2(float(token_data['x']), float(token_data['y'])))
        self.flipped = token_data['flipped']
        self.chit_type = AnimalType[token_data['chit_type']]
        self.count = int(token_data['count'])
        self.set_flip_sprite(self.flipped)
