import pygame
from pygame import Surface, Rect, Vector2, transform
from typing import Tuple


class Sprite:
    """
    A class used to represent a Sprite.

    Author: Yash Mahmud (32945795)

    ...

    Attributes
    ----------
    pos : tuple
        a tuple representing the position of the sprite (x, y)
    scale : int
        the scale of the sprite
    angle : int
        the angle of the sprite
    image : Surface
        the image of the sprite
    rect : Rect
        the rectangle area of the sprite

    Methods
    -------
    draw(surface):
        Draws the sprite on the given surface.
    set_sprite(image):
        Sets the sprite image and its rectangle area.
    set_scale(xscale, yscale):
        Sets the scale of the sprite.
    set_position(pos):
        Sets the position of the sprite.
    set_position_smooth(pos, amount):
        Spherically interpolates the position of the sprite.
    """

    def __init__(self, x: int, y: int, image: str, scale: tuple = (1, 1), angle: int = 0):
        """
        Author: Yash Mahmud (32945795)

        Constructs all the necessary attributes for the sprite object.

        Parameters
        ----------
            x : int
                x-coordinate of the sprite
            y : int
                y-coordinate of the sprite
            image : str
                the filename of the sprite image
            scale : tuple, optional
                the scale of the sprite (default is (1, 1))
            angle : int, optional
                the angle of the sprite (default is 0)
        """

        self.size = (0, 0)
        self.pos = Vector2(x, y)
        self.scale = scale
        self.angle = angle
        self.image, self.rect = self.set_sprite(image)

    def draw(self, surface: Surface) -> None:
        """
        Author: Yash Mahmud (32945795)

        Draws the sprite on the given surface.

        Parameters
        ----------
            surface : Surface
                the surface to draw the sprite on
        """

        surface.blit(self.image, (self.rect.x, self.rect.y))

    def set_sprite(self, image: str) -> Tuple[Surface, Rect]:
        """
        Author: Yash Mahmud (32945795)

        Sets the sprite image and its rectangle area.

        Parameters
        ----------
            image : str
                the filename of the sprite image

        Returns
        -------
            tuple
                a tuple containing the sprite image and its rect
        """

        self.filename = image
        sprite = pygame.image.load(f'assets/sprites/{image}.png').convert_alpha()

        self.size = (sprite.get_width(), sprite.get_height())

        self.image = transform.scale(sprite, (int(self.size[0] * self.scale[0]), int(self.size[1] * self.scale[1])))

        self.image = transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center=self.pos)

        return self.image, self.rect

    def set_scale(self, xscale, yscale) -> None:
        """
        Author: Yash Mahmud (32945795)

        Sets the scale of the sprite.

        Parameters
        ----------
            xscale : int
                the x-scale of the sprite
            yscale : int
                the y-scale of the sprite
        """

        self.scale = (xscale, yscale)

        sprite = pygame.image.load(f'assets/sprites/{self.filename}.png').convert_alpha()
        self.image = transform.scale(sprite, (self.size[0] * self.scale[0], self.size[1] * self.scale[1]))
        self.rect = self.image.get_rect(center=self.pos)

    def set_position(self, pos: Vector2) -> None:
        """
        Author: Yash Mahmud (32945795)

        Sets the position of the sprite.

        Parameters
        ----------
            pos : tuple
                a tuple representing the new position of the sprite (x, y)
        """

        self.pos = pos
        self.rect.center = pos

    def set_position_smooth(self, pos: Vector2, amount: float) -> None:
        """
        Author: Yash Mahmud (32945795)

        Spherically interpolates the position of the sprite.

        Parameters
        ----------
            pos : tuple
                a tuple representing the new position of the sprite (x, y)
            amount : float
                a float representing the amount of interpolation (the more the value,
                the faster the sprite will move.)
        """
        self.pos = Vector2.slerp(self.pos, pos, amount)

        self.set_position(self.pos)

