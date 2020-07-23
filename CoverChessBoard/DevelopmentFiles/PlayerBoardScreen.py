"""

Create an empty board. When the user presses a square, place a knight on that square.

"""
from CoverChessBoard.BoardSquares import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from functools import partial
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.colorpicker import Color
from kivy.graphics import Rectangle

def make_board():
    white = [1, 1, 1, 1]
    mild_green = [0, 0.6, 0.29, 1]
    dim = 8
    board = Board(white, mild_green, dim)
    return board

def setup_board():
    board = make_board()
    board.bind_squares_in_board()
    return board

def create_undo_button(board):
    undo_btn = Button(text="Undo",
                      background_normal='',
                      background_down='',
                      background_color=(0, 0, 0.14, 1),
                      color=(1, 1, 1, 0.7))
    undo_btn.bind(on_release=board.undo_callback)
    return undo_btn

def back_btn_callback(*args, screen_manager):
    screen_manager.current = "menu_screen"

def create_back_button(screen_manager):
    back_btn = Button(text="Go back",
                      background_normal='',
                      background_down='',
                      background_color=(0, 0, 0.14, 1),
                      color=(1, 1, 1, 0.7))
    back_btn.bind(on_release=partial(back_btn_callback, screen_manager=screen_manager))
    return back_btn

def create_player_board_layout(screen_manager):

    layout = BoxLayout(orientation='vertical')
    # Give background image to layout
    with layout.canvas.before:
        Color(0, 0, 0.14, 1)
        rect = Rectangle(size=(1000, 1000),
                         pos=layout.pos)
    board = setup_board()

    btn_layout = BoxLayout(orientation='horizontal')
    undo_btn = create_undo_button(board)
    back_btn = create_back_button(screen_manager)
    btn_layout.add_widget(back_btn)
    btn_layout.add_widget(undo_btn)
    btn_layout.size_hint = (1, 0.2)

    layout.add_widget(board.squares)
    layout.add_widget(btn_layout)

    return layout

def generate_layout():
    layout = RelativeLayout()
    # Give background image to layout
    with layout.canvas.before:
        Color(0, 0, 0.14, 1)
        rect = Rectangle(size=(1000, 1000),
                         pos=layout.pos)
    return layout

def setup_player_screen(screen_manager):
    player_board_layout = create_player_board_layout(screen_manager)
    player_screen = Screen(name="player_board_screen")
    player_screen.add_widget(player_board_layout)
    return player_screen

