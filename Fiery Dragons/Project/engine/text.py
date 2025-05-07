import pygame
from pygame import Color, Surface, Vector2


class Text:
    """
    A class used to represent a Text.

    Author: Yash Mahmud (32945795)

    ...

    Attributes
    ----------
    font : Font
        the font of the text
    pos : tuple
        a tuple representing the position of the text (x, y)
    color : Color
        the color of the text
    text : Surface
        the rendered text

    Methods
    -------
    draw(surface):
        Draws the text on the given surface.
    set_text(text):
        Sets the text to be rendered.
    set_alignment(alignment):
        Sets the alignment of the text.
    """

    def __init__(self, text: str, pos: Vector2, color: Color, font: str, alignment: str = 'topleft'):
        """
        Author: Yash Mahmud (32945795)

        Constructs all the necessary attributes for the text object.

        Parameters
        ----------
            text : str
                the text to be rendered
            pos : tuple
                a tuple representing the position of the text (x, y)
            color : Color
                the color of the text
            font : str
                the filename of the font
            alignment : str, optional
                the alignment of the text (default is 'topleft')
        """

        self.font = pygame.font.Font('assets/fonts/{0}.ttf'.format(font), 36)
        self.pos = pos
        self.color = color
        self.text = self.font.render(text, True, self.color)
        self.alignment = alignment
        self.set_alignment(self.alignment)

    def draw(self, surface: Surface) -> None:
        """
        Author: Yash Mahmud (32945795)

        Draws the text on the given surface.

        Parameters
        ----------
            surface : Surface
                the surface to draw the text on
        """

        surface.blit(self.text, self.text_rect)

    def set_text(self, text: str) -> None:
        """
        Author: Yash Mahmud (32945795)

        Sets the text to be rendered.

        Parameters
        ----------
            text : str
                the new text to be rendered
        """

        self.text = self.font.render(text, True, self.color)
        self.set_alignment(self.alignment)

    def set_alignment(self, alignment: str) -> None:
        """
        Author: Yash Mahmud (32945795)

        Sets the alignment of the text.

        Parameters
        ----------
            alignment : str
                the alignment of the text
        """
        if alignment not in ['center', 'topleft', 'topright', 'bottomleft', 'bottomright']:
            raise ValueError("Invalid alignment. Choose from 'center', 'topleft', 'topright', 'bottomleft', "
                             "or 'bottomright'.")
        self.alignment = alignment
        self.text_rect = self.text.get_rect(**{self.alignment: self.pos})