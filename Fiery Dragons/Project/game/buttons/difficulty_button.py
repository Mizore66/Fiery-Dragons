import pygame_gui
from pygame import Rect
from game.enums.difficultytypes import DifficultyType


class DifficultyButton:
    """
    Author: Yash Mahmud (32945795)

    A class used to represent a DifficultyButton, which is a subclass of Button.

    ...

    Attributes
    ----------
    menu : Menu
        the menu containing the button
    drop_down_menu : UIDropDownMenu
        the drop down menu for selecting the difficulty

    Methods
    -------
    events(event):
        Handles the events for the button.
    """
    def __init__(self, manager, x: int, y: int, size: tuple, angle: int, menu):
        """
        Author: Yash Mahmud (32945795)

        Constructs all the necessary attributes for the DifficultyButton object.

        Parameters
        ----------
            manager : UIManager
                the manager for the button
            x : int
                x-coordinate of the button
            y : int
                y-coordinate of the button
            size : tuple
                the size of the button
            angle : int
                the angle of the button
            menu : Menu
                the menu containing the button
        """
        self.menu = menu

        self.drop_down_menu = pygame_gui.elements.UIDropDownMenu(['Easy', 'Medium', 'Hard'],
                                                                 'Easy',
                                                                 Rect(x, y, size[0], size[1]),
                                                                 manager=manager)

    def events(self, event):
        """
        Author: Yash Mahmud (32945795)

        Handles the events for the button.

        Parameters
        ----------
            event : Event
                the event to handle
        """
        if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_element == self.drop_down_menu:
                new_diff = DifficultyType[self.drop_down_menu.selected_option[0].upper()]
                self.menu.set_difficulty(new_diff)
                print("Difficulty changed to " + new_diff.name)
