"""

Create an empty board. When the user presses a square, place a knight on that square.

"""
from CoverChessBoard.BoardSquares import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

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
    undo_btn = Button(text="Undo")
    undo_btn.size_hint = (0.5, 0.2)
    undo_btn.bind(on_release=board.undo_callback)
    return undo_btn

def create_player_board_layout():

    ## TODO place a small paragraph talking to the user
    ## TODO place a back button to go to previous screen
    layout = BoxLayout(orientation='vertical')

    board = setup_board()
    undo_btn = create_undo_button(board)

    layout.add_widget(board.squares)
    layout.add_widget(undo_btn)

    return layout

def setup_player_screen():
    player_board_layout = create_player_board_layout()
    player_screen = Screen(name="player_board_screen")
    player_screen.add_widget(player_board_layout)
    return player_screen

