"""
This module was built to contain the menu screen to navigate in the app.
"""
from CoverChessBoard.src.GUI.NavigationButtons import *
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.colorpicker import Color
from kivy.graphics import Rectangle
from kivy.uix.screenmanager import Screen


def create_title():
    """ Make a title for the menu.

    :return: Label
    """
    title_lbl = Label(text="What would you like to do?",
                      pos=(0, 250),
                      font_size='40sp',
                      color=(1, 1, 1, 0.7))
    return title_lbl


def generate_layout():
    """ Make a layout with a rectangle of a solid color.

    :return: A RelativeLayout to contain the navigation buttons.
    """
    layout = RelativeLayout()
    # Give background image to layout
    with layout.canvas.before:
        Color(0, 0, 0.14, 1)
        rect = Rectangle(size=(1000, 1000),
                         pos=layout.pos)
    return layout


def create_menu_layout(screen_manager):
    """ Bring together all navigation buttons in the menu.

    :param screen_manager: The manager for screens in the application.
    :return: A layout containing all navigation buttons.
    """
    layout = generate_layout()

    title_lbl = create_title()
    concept_btn = create_concept_button(screen_manager)
    conquer_btn = create_player_button(screen_manager)
    computer_btn = create_computer_button(screen_manager)

    layout.add_widget(title_lbl)
    layout.add_widget(concept_btn)
    layout.add_widget(conquer_btn)
    layout.add_widget(computer_btn)
    return layout


def setup_menuscreen(screen_manager):
    """ Make a menu screen for the application.

    :return: A screen with the menu for the application.
    """
    menu_layout = create_menu_layout(screen_manager)
    menu_screen = Screen(name="menu_screen")
    menu_screen.add_widget(menu_layout)
    return menu_screen
