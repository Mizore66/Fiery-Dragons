import json
import os

import pygame
import pygame_gui


class SaveWindow:
    """
    Author: Yash Mahmud (32945795)

    A class used to represent a SaveWindow, which is a window to save the game.

    ...

    Attributes
    ----------
    window : UIWindow
        the window to save the game
    manager : UIManager
        the manager for the window
    save_text : list
        the text to display the save information
    save_button : list
        the button to save the game
    load_button : list
        the button to load the game
    board : Board
        the board to save

    Methods
    -------
    update_save_info(i):
        Updates the save information for the slot.
    events(event):
        Handles the events for the window.
    """
    def __init__(self, manager, x: int, y: int, size: tuple, board):
        """
        Author: Yash Mahmud (32945795)

        Constructs all the necessary attributes for the SaveWindow object.

        Parameters
        ----------
            manager : UIManager
                the manager for the window
            x : int
                x-coordinate of the window
            y : int
                y-coordinate of the window
            size : tuple
                the size of the window
            board : Board
                the board to save
        """
        self.window = pygame_gui.elements.UIWindow(pygame.Rect(x, y, size[0], size[1]), manager,
                                                   window_display_title='Save Game',
                                                   resizable=False, draggable=False)

        self.manager = manager
        self.save_text = [None, None, None]
        self.save_button = [None, None, None]
        self.load_button = [None, None, None]

        for i in range(3):
            self.update_save_info(i)

            self.save_button[i] = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((346, 35 + (100 * i)), (100, 75)),
                text='Save',
                manager=self.manager,
                container=self.window)

            self.load_button[i] = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((450, 35 + (100 * i)), (100, 75)),
                text='Load',
                manager=self.manager,
                container=self.window)

        self.board = board

    def update_save_info(self, i):
        """
        Author: Yash Mahmud (32945795)

        Updates the save information for the slot.

        Parameters
        ----------
            i : int
                the slot to update
        """
        if os.path.exists('save_{0}.json'.format(i + 1)):
            with open('save_{0}.json'.format(i + 1), 'r') as file:
                data = json.load(file)

            game_data = data['game']
            text = 'Difficulty: ' + game_data['difficulty'] + ', CPU Players: ' + str(game_data['cpu_count'])
        else:
            text = 'No save data.'

        self.save_text[i] = pygame_gui.elements.UITextBox('Slot {0} \n'.format(i + 1) + text,
                                                          pygame.Rect(50, 35 + (100 * i), 290, 75),
                                                          self.manager, container=self.window)

    def events(self, event):
        """
        Author: Yash Mahmud (32945795)

        Handles the events for the window.

        Parameters
        ----------
            event : Event
                the event to handle
        """
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            for i in range(3):
                if event.ui_element == self.save_button[i]:
                    print('Game saved in Slot ' + str(i + 1) + '.')
                    self.board.save('save_' + str(i + 1) + '.json')
                    self.update_save_info(i)
                if event.ui_element == self.load_button[i]:
                    print('Loading Slot ' + str(i + 1) + '.')
                    try:
                        self.board.load('save_' + str(i + 1) + '.json')
                    except:
                        print('No save data in Slot ' + str(i + 1) + '.')
        if event.type == pygame_gui.UI_WINDOW_CLOSE:
            self.board.window_open = False
