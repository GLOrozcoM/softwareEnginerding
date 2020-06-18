"""
Figure out how to create a chess board in Kivy.
Prototype a solution that makes sense for movement of pieces.

ideas:
- Work with a 2d array of 1 and 0. All 0, except 1 is current piece.
If entry reads a 0 display original, 1 shows position of piece.
- Track entries this way.
- Multiple buttons, with the "piece button". Possible class of board.
--> Create a board of buttons.

"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from CoverChessBoard import ChessBoard

### Function development begins

def make_square(column, square_color):
    """ Create a single chess square. Square is a button so user can press it and make moves.

    :param column: Column in a chess board the square gets placed in
    :param square_color: Color of the square
    :return: None
    """
    column.add_widget(Button(background_normal = '',
                             background_color = square_color))

def add_squares_to_column(column, color_one, color_two):
    """

    :param column:
    :param color_one:
    :param color_two:
    :return:
    """
    for i in range(0, 8):
        if (i % 2) == 0:
            make_square(column, color_one)
        else:
            make_square(column, color_two)

def make_column(parity):
    """

    :param parity:
    :return:
    """
    column = BoxLayout(orientation = 'vertical')

    # Colors for board - RGBA format, scaled to be between 0 and 1
    mild_green = [0, 0.6, 0.29, 1]
    white = [1, 1, 1, 1]

    # A column in an odd number must start with with light color and end in dark color
    if parity == 'odd':
        add_squares_to_column(column, white, mild_green)
    # A column in an even number must start with dark color and end in light color
    else:
        add_squares_to_column(column, mild_green, white)

    return column

def add_column_to_row(row, parity):
    """

    :param row:
    :param parity:
    :return:
    """
    vertical_buttons = make_column(parity)
    row.add_widget(vertical_buttons)

def fill_rows():
    """

    :return:
    """
    rows = BoxLayout(orientation = 'horizontal')
    for i in range(0, 8):
        if (i % 2) != 0:
            add_column_to_row(rows, 'odd')
        else:
            add_column_to_row(rows, 'even')
    return rows


###### Function development ends

class Board(App):

    def build(self):
        white = [0, 0, 0, 0]
        mild_green = [0, 0.6, 0.29, 1]
        chess_board = ChessBoard(white, mild_green)
        print(type(chess_board.squares))
        return chess_board.squares


the_board = Board()
the_board.run()