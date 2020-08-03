"""
This module was built to contain the first screen to welcome user.
"""
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.colorpicker import Color
from kivy.graphics import Rectangle
from functools import partial
from kivy.uix.screenmanager import Screen


def navigate_menu(screen_manager, *args):
    """ Take the user to the screen showing a menu.

    :param screen_manager: The manager for screens in the application.
    :param args: Extra arguments.
    :return: None.
    """
    screen_manager.current = "menu_screen"
    return None


def create_menu_button(screen_manager):
    """ Make a button to take the user to the menu.

    :param screen_manager: The manager for screens in the application.
    :return:
    """
    continue_btn = Button(text="Press here to start",
                          background_normal='',
                          background_down='',
                          background_color=(0, 0, 0.14, 1),
                          color=(1, 1, 1, 0.7))
    continue_btn.bind(on_release=partial(navigate_menu, screen_manager))
    return continue_btn


def create_version():
    """ Write the version to the screen.

    :return: A label holding the version.
    """
    version = Label(text="Version 1.0",
                    pos=(650, 10),
                    size_hint=(0.10, 0.10),
                    color=(1, 1, 1, 0.7))
    return version


def create_subtitle():
    """ Make a subtitle for the welcome screen.

    :return: A label containing the subtitle.
    """
    subtitle = Label(text="Use the knight to visit every square on the board or "
                          "have a computer do it for you.",
                     pos=(0, 180),
                     color=(1, 1, 1, 0.7))
    return subtitle


def create_title():
    """ Give the title to the welcome screen.

    :return: A label containing the title.
    """
    title = Label(text="Conquer the chess board!",
                  pos=(0, 250),
                  font_size='50sp',
                  color=(1, 1, 1, 0.7))
    return title


def create_author():
    """ Make the author label.

    :return: A label containing the author.
    """
    author = Label(text="G.L.Orozco-Mulfinger",
                   pos=(80, 10),
                   size_hint=(0.1, 0.1),
                   color=(1, 1, 1, 0.7))
    return author


def generate_layout():
    """ Make a layout to place welcome screen on.

    :return: A layout to place welcome screen items on.
    """
    layout = BoxLayout(orientation="horizontal")
    # Give background image to layout
    with layout.canvas.before:
        Color(0, 0, 0.14, 1)
        rect = Rectangle(size=(5000, 5000),
                         pos=layout.pos)
    return layout


def create_welcome_layout(screen_manager):
    """ Bring together items for the general_layout in the welcome screen.

    :param screen_manager: The manager for screens in the application.
    :return: A general_layout containing the welcome screen.
    """
    general_layout = generate_layout()

    author_layout = AnchorLayout(anchor_x="center", anchor_y="bottom")
    author = create_author()
    author_layout.add_widget(author)

    button_title_layout = BoxLayout(orientation="vertical")
    title = create_title()
    subtitle = create_subtitle()
    continue_btn = create_menu_button(screen_manager)
    button_title_layout.add_widget(title)
    button_title_layout.add_widget(subtitle)
    button_title_layout.add_widget(continue_btn)

    version_layout = AnchorLayout(anchor_x="center", anchor_y="bottom")
    version = create_version()
    version_layout.add_widget(version)

    general_layout.add_widget(author_layout)
    general_layout.add_widget(button_title_layout)
    general_layout.add_widget(version_layout)

    return general_layout


def setup_welcome_screen(screen_manager):
    """ Create the welcome screen for the user.

    :param screen_manager: The manager for screens in the application.
    :return: The screen containing the welcome message for the user.
    """
    welcome_layout = create_welcome_layout(screen_manager)
    welcome_screen = Screen(name="welcome_screen")
    welcome_screen.add_widget(welcome_layout)
    return welcome_screen