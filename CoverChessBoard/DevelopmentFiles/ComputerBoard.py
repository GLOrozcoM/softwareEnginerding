"""

Create an empty board. When the user presses a square, place a knight on that square.

"""

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
    top_layout = instance.parent.parent

    # Find the piece's position in the sibling layout for a button
    start_position = ''
    piece = None
    board = None
    for layout in top_layout.children:
        if isinstance(layout, GridLayout):
            board_squares = layout
            for obj in layout.children:
                if isinstance(obj, Piece):
                    piece = obj
                    start_position = piece.square.position

    move_list = get_path(start_position, "../SolutionPaths/knight_tour.txt")
    seconds = 3
    for move in move_list:
        # TODO implement class/method that assures this method is linked to board object
        Clock.schedule_once(partial(move_piece_to_str_ij, move, board_squares, piece), seconds)
        seconds += 0.1

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

