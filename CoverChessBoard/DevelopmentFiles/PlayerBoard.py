"""

Create an empty board. When the user presses a square, place a knight on that square.

"""
from CoverChessBoard.BoardSquares import *
from kivy.uix.boxlayout import BoxLayout

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

def create_player_board_layout():

    ## TODO place a small paragraph talking to the user
    ## TODO place a back button to go to previous screen
    layout = BoxLayout(orientation='vertical')

    board = setup_board()

    return board.squares
