"""

Create an empty board. When the user presses a square, place a knight on that square.

"""

import os

from kivy.app import App
from CoverChessBoard.BoardSquares import *
from CoverChessBoard.ChessPieces import *
from CoverChessBoard.FindPath import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.clock import Clock
from functools import partial
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.colorpicker import Color
from kivy.graphics import Rectangle

class BoardScreen(Screen):

    def __init__(self, name):
        super().__init__(name = name)

        # A chess board object, not just the squares
        self. board = None

def setup_computer_board_screen(screen_manager):
    # Over arching screen
    layout = BoxLayout(orientation='vertical')
    # Give background image to layout
    with layout.canvas.before:
        Color(0, 0, 0.14, 1)
        rect = Rectangle(size=(1000, 1000),
                         pos=layout.pos)

    # Board
    screen = BoardScreen(name = "computer_board_screen")
    screen.board = setup_board()

    # Notice squares get added not the board itself
    layout.add_widget(screen.board.squares)

    # Buttons
    btn_layout = BoxLayout(orientation='horizontal')
    start_btn = create_start_button()
    back_btn = create_back_button(screen_manager)
    btn_layout.add_widget(back_btn)
    btn_layout.add_widget(start_btn)
    btn_layout.size_hint = (1, 0.2)

    layout.add_widget(btn_layout)
    screen.add_widget(layout)
    return screen

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

def start_solution_callback(instance, *largs):
    """ Start the process for seeing the board populated by the piece.

    :param instance:
    :param largs:
    :return:
    """
    # Acces the layout holding both the button and the board squares
    # -- go from current button, to grid layout, to screen, to board object in screen.
    board = instance.parent.parent.parent.board

    start_position = ''
    for obj in board.squares.children:
        if isinstance(obj, Piece):
            start_position = obj.square.position
    if board.piece:
        move_list = get_path(start_position, "../SolutionPaths/knight_tour.txt")
        seconds = 3
        for move in move_list:
            Clock.schedule_once(partial(board.move_piece_to_str_ij, move, board.piece), seconds)
            seconds += 0.1
    else:
        print("Place the piece on the board before you try to solve anything!")

def create_start_button():
    start_btn = Button(text="Start solution",
                       pos=(100, 100),
                       background_normal='',
                       background_down='',
                       background_color=(0, 0, 0.14, 1),
                       color=(1, 1, 1, 0.7))
    start_btn.bind(on_release=start_solution_callback)
    return start_btn
