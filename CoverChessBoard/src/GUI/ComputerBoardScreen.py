"""
This module was built to contain the screen where a user can see a computer generated solution to the knight's tour.
"""
from CoverChessBoard.src.backend.BoardSquares import *
from CoverChessBoard.src.backend.ChessPieces import *
from CoverChessBoard.src.GUI.NavigationButtons import *
from CoverChessBoard.src.backend.FindSolutionPath import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from functools import partial
from kivy.uix.screenmanager import Screen
from kivy.uix.colorpicker import Color
from kivy.graphics import Rectangle


class BoardScreen(Screen):
    """
    Make a screen object with an extra attribute - the chess board.
    """

    def __init__(self, name):
        super().__init__(name=name)

        # A chess board object, not just the squares
        self.board = None


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


def setup_computer_board_screen(screen_manager):
    """ Bring together elements for the screen where a user can see the computer generated solution.

    :param screen_manager: The manager for screens in the application.
    :return: The screen containing the board where a computer can show the solution.
    """
    layout = BoxLayout(orientation='vertical')

    # Give background image to layout
    with layout.canvas.before:
        Color(0, 0, 0.14, 1)
        rect = Rectangle(size=(1000, 1000),
                         pos=layout.pos)
    screen = BoardScreen(name="computer_board_screen")
    screen.board = setup_board()

    # Notice squares get added not the board itself
    layout.add_widget(screen.board.squares)

    # Buttons
    btn_layout = BoxLayout(orientation='horizontal')

    start_solution_btn = create_solution_button()
    back_btn = create_back_button(screen_manager)
    reset_btn = create_reset_button(screen_manager)

    btn_layout.add_widget(back_btn)
    btn_layout.add_widget(start_solution_btn)
    btn_layout.add_widget(reset_btn)

    btn_layout.size_hint = (1, 0.2)

    layout.add_widget(btn_layout)
    screen.add_widget(layout)
    return screen


def start_solution_callback(instance, *largs):
    """ Execute the process for seeing the board covered by the knight piece.

    :param instance: The button that got pressed.
    :param largs: Extra arguments.
    :return: None.
    """
    # Get the board associated with this screen
    # -- go from current button, to grid layout, to screen, to board object in screen.
    board = instance.parent.parent.parent.board

    # Determine where the piece is on the board
    start_position = ''
    for obj in board.squares.children:
        if isinstance(obj, Piece):
            start_position = obj.square.position
    # Only if a piece is present is a solution found for it
    if board.piece:
        move_list = get_path(start_position, "../../solution_paths/knight_tour.txt")
        seconds = 0.5
        for move in move_list:
            Clock.schedule_once(partial(board.move_piece_to_str_ij, move, board.piece), seconds)
            seconds += 0.1
    else:
        print("Place the piece on the board before you try to solve anything!")


def create_solution_button():
    """ Make a button that will find the solution for the knight's tour.

    :return: A button to start the solution of the knight's tour.
    """
    start_btn = Button(text="Start solution",
                       pos=(100, 100),
                       background_normal='',
                       background_down='',
                       background_color=(0, 0, 0.14, 1),
                       color=(1, 1, 1, 0.7))
    start_btn.bind(on_release=start_solution_callback)
    return start_btn


def reset_button_callback(instance, screen_manager):
    """ Activate the board resetting process.

    :return: None
    """
    # Get the board associated with this screen
    # -- go from current button, to grid layout, to screen
    layout_for_screen = instance.parent.parent

    # Remove previous board layout　and buttons
    layout_for_screen.children.pop()
    layout_for_screen.children.pop()

    new_board_screen = setup_computer_board_screen(screen_manager)
    layout_for_screen.add_widget(new_board_screen)
    return

def create_reset_button(screen_manager):
    """ Make a button that will reset the board for the user to try a different solution.

    :return: A button to reset the board.
    """
    reset_btn = Button(text="Reset board",
                       pos=(100, 100),
                       background_normal='',
                       background_down='',
                       background_color=(0, 0, 0.14, 1),
                       color=(1, 1, 1, 0.7))
    reset_btn.bind(on_release=partial(reset_button_callback, screen_manager=screen_manager))
    return reset_btn
