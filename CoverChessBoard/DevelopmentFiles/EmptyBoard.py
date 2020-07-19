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


def str_ij_to_int(ij):
    i = int(ij[0])
    j = int(ij[1])
    return i, j

def place_piece_at_index(square, piece, index, children):
    """ Take a piece and place it on the square in a board. Index is the position of the
    square in the children list for the board.

    :param square: Destination square for the piece
    :param piece:
    :param index:
    :param children:
    :return:
    """
    # Remove the square occupying the space on board
    children.remove_widget(square)

    # Makes sure piece is associated with the new square
    piece.square = square

    # Place the piece at the destination square
    children.add_widget(piece, index)

    # Recalculate the possible moves for the piece based on the new position
    piece.make_move_list(children)

    return children

def color_square(position):
    """ Takes the position of a square and gives it the appropriate color
    on the chess board.

    :param position:
    :return:
    """
    i, j = str_ij_to_int(position)
    if (i + j) % 2 == 0:
        white = [1, 1, 1, 1]
        color = white
    else:
        mild_green = [0, 0.6, 0.29, 1]
        color = mild_green
    return color

def square_pressed_place_piece(piece, instance):
    """ First event expected from user. Place the piece on the square that got pressed.

    :param piece:
    :param instance:
    :return:
    """

    # Piece should go on the board only if it isn't already there!
    board = instance.parent
    piece_present = False
    for obj in board.children:
        if isinstance(obj, Piece):
            piece_present = True
    if piece_present == False:
        # Find which square got pressed on the board
        current_square_index = board.children.index(instance)

        # Remove the destination square, place piece there
        place_piece_at_index(instance, piece, current_square_index, board)
    else:
        square_pressed_piece_on_board(piece, instance)

def square_pressed_piece_on_board(piece, instance):
        """ Actions to take when the a square on the board gets pressed and
        the piece is already present.

        :param piece:
        :param instance:
        :return:
        """

        # Find which square got pressed on the board
        board = instance.parent
        current_square_index = board.children.index(instance)

        # Only move the piece if the piece can move to that square
        if instance in piece.possible_moves:
            # If the piece hasn't been pressed, don't move it
            if piece.state == "normal":
                return

            # Remove the piece, place a new square there
            replace_piece_square(board, piece)
            # Remove the destination square, place piece there
            place_piece_at_index(instance, piece, current_square_index, board)

def replace_piece_square(board, piece):
    # Where the piece was on the board
    occupied_square_index = board.children.index(piece)
    board.remove_widget(piece)

    # Get the appropriate light or dark color for the square
    # and create a new square
    color = color_square(piece.square.position)
    occupied_square = Square(piece.square.position, color)

    # Give tint to indicate a piece has already been on this square
    dark_blue = [0, 0.30, 1, 0.9]
    occupied_square.background_color = dark_blue

    # Uncomment to allow moving back to a square the piece
    # has stepped on
    # occupied_square.bind(on_release = self.square_pressed)

    # Place a tinted square back on the board
    board.add_widget(occupied_square, occupied_square_index)

def bind_squares_in_board(board):
    """ Bind button events to squares on the chess board.

    :param board:
    :return:
    """

    for obj in board.squares.children:
        # Only bind the square objects, not the Piece
        if not isinstance(obj, Piece):
            obj.bind(on_release=partial(square_pressed_place_piece, board.piece))

def find_square(i, j, board):
    """ Get the square in ith row, jth column in the board.
    Starting from 1st row

    :param i: Row
    :param j: Column
    :return:
    """
    for square in board.children:
        # Position encoded from 1th row, 1th column
        position = str(i) + str(j)
        if position == square.position:
            return square
    print("Square not found for combination of i and j")
    return None

def move_piece_to_str_ij(str_ij, board, piece, *largs):
    """ Have the program move the piece to an ij position on the board.

    :param str_ij:
    :param board:
    :param piece:
    :param largs:
    :return:
    """
    # Replace the square where the piece originates
    replace_piece_square(board, piece)

    # Move the piece to ij position on board
    i, j = str_ij_to_int(str_ij)
    destination_square = find_square(i, j, board)
    children = board.children
    index_to_move = children.index(destination_square)
    place_piece_at_index(destination_square, piece, index_to_move, board)

def make_board():
    white = [1, 1, 1, 1]
    mild_green = [0, 0.6, 0.29, 1]
    dim = 8
    board = SquaresLayout(white, mild_green, dim)
    return board

def setup_board():
    board = make_board()
    piece = Knight()
    board.piece = piece
    bind_squares_in_board(board)
    return board

def start_solution_callback(instance, *largs):
    """ Start the process for seeing the board populated by the piece.

    :param instance:
    :param largs:
    :return:
    """
    top_layout = instance.parent.parent
    # Find the piece's position in the sibling layout for a button
    start_position = ''
    piece = None
    board = None
    for layout in top_layout.children:
        if isinstance(layout, GridLayout):
            board = layout
            for obj in layout.children:
                if isinstance(obj, Piece):
                    piece = obj
                    start_position = piece.square.position

    move_list = get_path(start_position, "../SolutionPaths/knight_tour.txt")
    seconds = 3
    for move in move_list:
        Clock.schedule_once(partial(move_piece_to_str_ij, move, board, piece), seconds)
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

def create_empty_board_layout():

    layout = BoxLayout(orientation='vertical')

    board = setup_board()
    btn_layout = create_start_button()

    # Notice squares get added not the board itself
    layout.add_widget(board.squares)
    layout.add_widget(btn_layout)

    return layout

