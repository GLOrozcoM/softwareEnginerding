"""
This module was built to contain the board on which a player can make moves.
"""
from CoverChessBoard.src.backend.BoardSquares import *
from CoverChessBoard.src.GUI.NavigationButtons import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.colorpicker import Color
from kivy.graphics import Rectangle


def setup_board():
    """ Get a chess board ready for the program with colors and dimensions.

    :return: The prepared chess board.
    """
    white = [1, 1, 1, 1]
    mild_green = [0, 0.6, 0.29, 1]
    dim = 8
    board = Board(white, mild_green, dim)
    board.bind_squares_in_board()
    return board


def create_undo_button(board):
    """ Create a button for the player to undo a move.

    :param board: The chess board associated with the undo button.
    :return:
    """
    undo_btn = Button(text="Undo",
                      background_normal='',
                      background_down='',
                      background_color=(0, 0, 0.14, 1),
                      color=(1, 1, 1, 0.7))
    undo_btn.bind(on_release=board.undo_callback)
    return undo_btn


def create_player_board_layout(screen_manager):
    """ Generate a layout containing the player board and buttons.

    :param screen_manager: The manager for screens in the application.
    :return: A BoxLayout with the board and buttons for the screen.
    """

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


def setup_player_screen(screen_manager):
    """ Create and setup the screen to hold the board a player can try solving the tour on.

    :param screen_manager: The manager for screens in the application.
    :return: The screen holding the player board.
    """
    player_board_layout = create_player_board_layout(screen_manager)
    player_screen = Screen(name="player_board_screen")
    player_screen.add_widget(player_board_layout)
    return player_screen

