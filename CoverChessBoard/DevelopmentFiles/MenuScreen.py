"""

Menu screen to navigate app.

"""

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.colorpicker import Color
from kivy.graphics import Rectangle
from functools import partial
from kivy.uix.screenmanager import Screen

def navigate_player_board(screen_manager, *args):
    screen_manager.current = "player_board_screen"

def navigate_computer_board(screen_manager, *args):
    screen_manager.current = "computer_board_screen"

def create_computer_button(screen_manager):
    computer_btn = Button(text="Have the computer conquer for you",
                          pos=(325, 110),
                          size_hint=(0.2, 0.2),
                          background_normal='',
                          background_down='',
                          background_color=(0, 0, 0.14, 1),
                          color=(1, 1, 1, 0.7))
    computer_btn.bind(on_release = partial(navigate_computer_board, screen_manager))
    return computer_btn

def create_conquer_button(screen_manager):
    conquer_btn = Button(text="Try to conquer the board yourself",
                         pos=(325, 210),
                         size_hint=(0.2, 0.2),
                         background_normal='',
                         background_down='',
                         background_color=(0, 0, 0.14, 1),
                         color=(1, 1, 1, 0.7))
    conquer_btn.bind(on_release=partial(navigate_player_board, screen_manager))
    return conquer_btn

def create_concept_button():
    concept_btn = Button(text="Get the process explained",
                         pos=(325, 310),
                         size_hint=(0.2, 0.2),
                         background_normal='',
                         background_down='',
                         background_color=(0, 0, 0.14, 1),
                         color=(1, 1, 1, 0.7))
    ## TODO Create a conceptual screen for what the process is all about
    return concept_btn

def create_title():
    title_lbl = Label(text="What would you like to do?",
                      pos=(0, 250),
                      font_size='40sp',
                      color=(1, 1, 1, 0.7))
    return title_lbl

def generate_layout():
    layout = RelativeLayout()
    # Give background image to layout
    with layout.canvas.before:
        Color(0, 0, 0.14, 1)
        rect = Rectangle(size=(1000, 1000),
                         pos=layout.pos)
    return layout

def create_menu_layout(screen_manager):
    layout = generate_layout()

    title_lbl = create_title()
    concept_btn = create_concept_button()
    conquer_btn = create_conquer_button(screen_manager)
    computer_btn = create_computer_button(screen_manager)

    layout.add_widget(title_lbl)
    layout.add_widget(concept_btn)
    layout.add_widget(conquer_btn)
    layout.add_widget(computer_btn)
    return layout

def setup_menuscreen(sm):
    """ Make a menu screen for the application.

    :return:
    """
    menu_layout = create_menu_layout(sm)
    menu_screen = Screen(name="menu_screen")
    menu_screen.add_widget(menu_layout)
    return menu_screen
