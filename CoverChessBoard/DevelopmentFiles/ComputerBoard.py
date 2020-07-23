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

class BoardScreen(Screen):

    def __init__(self, name):
        super().__init__(name = name)

        # A chess board object, not just the squares
        self. board = None

def set_up_computer_board_screen():
    # Over arching screen
    layout = BoxLayout(orientation='vertical')

    # Board
    screen = BoardScreen(name = "computer_board_screen")
    screen.board = setup_board()

    # Notice squares get added not the board itself
    layout.add_widget(screen.board.squares)

    # Button
    btn_layout = create_start_button()
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

def start_solution_callback(instance, *largs):
    """ Start the process for seeing the board populated by the piece.

    :param instance:
    :param largs:
    :return:
    """
    # Acces the layout holding both the button and the board squares
    # -- go from current button, to grid layout, to screen, to board object in screen.
    board = instance.parent.parent.parent.board

    # Find the piece's position in the sibling layout for a button
    start_position = ''
    for obj in board.squares.children:
        if isinstance(obj, Piece):
            start_position = obj.square.position
    if board.piece:
        move_list = get_path(start_position, "../SolutionPaths/knight_tour.txt")
        seconds = 3
        count = 0
        for move in move_list:
            Clock.schedule_once(partial(board.move_piece_to_str_ij, move, board.piece, count), seconds)
            count += 1
            seconds += 0.1
    else:
        print("Place the piece on the board before you try to solve anything!")

def create_start_button():
    btn_layout = AnchorLayout()
    start_btn = Button(text="Start solution",
                       pos=(100, 100),
                       background_normal='',
                       background_down='',
                       background_color=(0, 0, 0.14, 1),
                       color=(1, 1, 1, 0.7))
    start_btn.bind(on_release=start_solution_callback)
    btn_layout.add_widget(start_btn)
    btn_layout.size_hint = (1, 0.2)
    return btn_layout

def create_computer_board_layout():

    layout = BoxLayout(orientation='vertical')

    board = setup_board()
    btn_layout = create_start_button()

    # Notice squares get added not the board itself
    layout.add_widget(board.squares)
    layout.add_widget(btn_layout)

    return layout

