import pygame_gui
from pygame import Rect


class CPUButton:
    """
    Author: Yash Mahmud (32945795)

    A class used to represent a CPUButton, which is a subclass of Button.

    ...

    Attributes
    ----------
    menu : Menu
        the menu containing the button
    cpu_count : int
        the number of CPU players
    drop_down_menu : UIDropDownMenu
        the drop down menu for selecting the number of CPU players

    Methods
    -------
    events(event):
        Handles the events for the button.
    """
    def __init__(self, manager, x: int, y: int, size: tuple, angle: int, menu, cpu_count: int):
        """
        Author: Yash Mahmud (32945795)

        Constructs all the necessary attributes for the CPUButton object.

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
            cpu_count : int
                the number of CPU players
        """
        self.menu = menu
        self.cpu_count = cpu_count

        self.drop_down_menu = pygame_gui.elements.UIDropDownMenu(['0 CPU Players', '1 CPU Player', '2 CPU Players', '3 CPU Players'],
                                                                 '0 CPU Players',
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
                new_cpu = int(self.drop_down_menu.selected_option[0][0])
                self.menu.set_cpu_count(new_cpu)
                print("CPU Players changed to " + str(new_cpu))
