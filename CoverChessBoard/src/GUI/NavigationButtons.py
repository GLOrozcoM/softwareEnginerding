"""
This module was built to encapsulate the buttons a user uses to navigate screens in the app.
"""
from kivy.uix.button import Button
from functools import partial


def navigate_player_board(screen_manager, *args):
    """ Take the player to the screen where they can try solving the tour.

    :param screen_manager: The manager for screens in the application.
    :param args: Extra arguments.
    :return: None.
    """
    screen_manager.current = "player_board_screen"
    return None


def navigate_computer_board(screen_manager, *args):
    """ Take the player to the screen containing the computer solution to the tour.

    :param screen_manager: The manager for screens in the application.
    :param args: Extra arguments.
    :return: None.
    """
    screen_manager.current = "computer_board_screen"
    return None


def navigate_explanation(screen_manager, *args):
    """ Take the user to the screen showing an explanation for the program.

    :param screen_manager: The manager for screens in the application.
    :param args: Extra arguments.
    :return: None.
    """
    screen_manager.current = "explanation_screen"
    return None


def create_computer_button(screen_manager):
    """ Make a button to take the user to see the computer generated solution.

    :param screen_manager: The manager for screens in the application.
    :return: The button to take the user to the computer generated solution.
    """
    computer_btn = Button(text="Have the computer conquer for you",
                          pos=(325, 110),
                          size_hint=(0.2, 0.2),
                          background_normal='',
                          background_down='',
                          background_color=(0, 0, 0.14, 1),
                          color=(1, 1, 1, 0.7))
    computer_btn.bind(on_release = partial(navigate_computer_board, screen_manager))
    return computer_btn


def create_player_button(screen_manager):
    """ Make a button to take the user to the board where they can try solving the tour.

    :param screen_manager: The manager for screens in the application.
    :return: The button to take the user to the player board.
    """
    conquer_btn = Button(text="Try to conquer the board yourself",
                         pos=(325, 210),
                         size_hint=(0.2, 0.2),
                         background_normal='',
                         background_down='',
                         background_color=(0, 0, 0.14, 1),
                         color=(1, 1, 1, 0.7))
    conquer_btn.bind(on_release=partial(navigate_player_board, screen_manager))
    return conquer_btn


def create_concept_button(screen_manager):
    """ Make a button that takes the user to see an explanation of the program.

    :param screen_manager: The manager for screens in the application.
    :return: Button taking the user to the explanation.
    """
    concept_btn = Button(text="Get the process explained",
                         pos=(325, 310),
                         size_hint=(0.2, 0.2),
                         background_normal='',
                         background_down='',
                         background_color=(0, 0, 0.14, 1),
                         color=(1, 1, 1, 0.7))
    concept_btn.bind(on_release=partial(navigate_explanation, screen_manager))
    return concept_btn


def back_btn_callback(*args, screen_manager):
    """ Send the user back to the menu screen if called.

    :param args: Extra arguments that could come in.
    :param screen_manager: The manager for screens in the application.
    :return: None
    """
    screen_manager.current = "menu_screen"
    return None


def create_back_button(screen_manager):
    """ Create a button for the user to go back to the menu screen.

    :param screen_manager: The manager for screens in the application.
    :return: The back button object.
    """
    back_btn = Button(text="Go back",
                      background_normal='',
                      background_down='',
                      background_color=(0, 0, 0.14, 1),
                      color=(1, 1, 1, 0.7))
    back_btn.bind(on_release=partial(back_btn_callback, screen_manager=screen_manager))
    return back_btn