"""

Inform the user about picking a square to place the piece on.

"""
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.colorpicker import Color
from kivy.graphics import Rectangle
from functools import partial


def create_instruction():
    title_lbl = Label(text="Press on a square in the next screen to place a piece.",
                      pos=(0, 210),
                      font_size='25sp',
                      color=(1, 1, 1, 0.7))
    return title_lbl

def navigate_board(screen_manager, *args):
    # TODO change to board screen
    print(screen_manager.previous())
    screen_manager.current = "player_board_screen"

def create_continue_button(screen_manager):
    continue_btn = Button(text="Take me to the board.",
                          pos=(325, 250),
                          size_hint=(0.2, 0.2),
                          background_normal='',
                          background_down='',
                          background_color=(0, 0, 0.14, 1),
                          color=(1, 1, 1, 0.7))
    continue_btn.bind(on_release=partial(navigate_board, screen_manager))
    return continue_btn

def generate_layout():
    layout = RelativeLayout()
    # Give background image to layout
    with layout.canvas.before:
        Color(0, 0, 0.14, 1)
        rect = Rectangle(size=(1000, 1000),
                         pos=layout.pos)
    return layout

def create_choose_square_layout(screen_manager):
    layout = generate_layout()

    instruction_lbl = create_instruction()
    continue_btn = create_continue_button(screen_manager)

    layout.add_widget(instruction_lbl)
    layout.add_widget(continue_btn)
    return layout