"""
This module was built to contain the board used to display the piece tour.
"""

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from functools import partial
from CoverChessBoard.src.ChessPieces import *


class Square(Button):

    def __init__(self, ij, color, text=""):
        super().__init__(text=text)
        self.background_color = color

        # Position on the board in matrix notation. Assume i and j both begin at 1.
        # i is the row, and j is the column
        self.position = ij
        self.i = int(ij[0])
        self.j = int(ij[1])


class Board():

    def __init__(self, light_color, dark_color, dimension):
        self.light_color = light_color
        self.dark_color = dark_color

        # Squares given in a GridLayout
        self.squares = self.make_squares(light_color, dark_color, dimension)

        # Assume only a single piece will ever be on the squares
        self.piece = None

        # How many movements the player has gone through
        self.move_count = 0

        # Track what movements are made in case the player wants to undo
        # -- holds tuples, first entry is the square object, second entry is the index of
        # -- square object in the children list
        self.move_stack = []

    ### ij position methods ###############################

    def str_ij_to_int(self, ij):
        """ Get integers from a string.

        :param ij: A string of two integers denoting a matrix. Example: "12"
        :return:
        """
        i = int(ij[0])
        j = int(ij[1])
        return i, j

    def move_piece_to_str_ij(self, str_ij, piece,*largs):
        """ Have the program move the piece to an ij position on the board.

        :param str_ij: A string with matrix coordinates. Example: '23'
        :param board: The chess board.
        :param piece: The chess piece.
        :param largs: Accept extra arguments since may be a callback method.
        :return: None
        """
        # Replace the square where the piece originates
        self.replace_piece_square(self.squares, piece)

        # Move the piece to ij position on board
        i, j = self.str_ij_to_int(str_ij)
        destination_square = self.find_square(i, j)
        children = self.squares.children
        index_to_move = children.index(destination_square)
        self.place_piece_at_index(destination_square, piece, index_to_move)

    #######################################################

    ### Square creation methods ###########################

    def color_square(self, position):
        """ Takes the position of a square and gives it the appropriate color
        on the chess board.

        :param position: A string coordinate for a matrix entry. Example: '11'.
        :return: Color to give the square.
        """
        i, j = self.str_ij_to_int(position)
        if (i + j) % 2 == 0:
            white = [1, 1, 1, 1]
            color = white
        else:
            mild_green = [0, 0.6, 0.29, 1]
            color = mild_green
        return color

    def make_square(self, text, color):
        """ Create a square object.

        :param text: Text to display for the square.
        :param color: Color to give the square.
        :return: A square object.
        """
        return Square(text, color)

    def make_squares(self, light_color, dark_color, n):
        """ Create an n x n grid of squares.

        :param light_color: Lighter color on the chess board.
        :param dark_color: Darker color on the chess board.
        :param n: The dimension of the grid.
        :return: A grid layout holding n columns.
        """
        grid = GridLayout(cols=n)
        for i in range(0, n):
            for j in range(0, n):
                sum = i + j
                if (sum % 2) == 0:
                    text = str(i + 1) + str(j + 1)
                    square = self.make_square(text, light_color)
                    grid.add_widget(square)
                else:
                    text = str(i + 1) + str(j + 1)
                    square = self.make_square(text, dark_color)
                    grid.add_widget(square)
        return grid

    #######################################################

    #### Event handling methods ###########################

    def bind_squares_in_board(self):
        """ Bind button events to squares on the chess board.

        :return: None
        """
        for obj in self.squares.children:
            # Only bind the square objects, not the Piece object
            if not isinstance(obj, Piece):
                obj.bind(on_release=partial(self.square_pressed))
        return

    def square_pressed(self, instance):
        """ First event expected from user. Place the piece on the square that got pressed.
        This is a callback method.

        :param instance: Instance of the button pressed.
        :return:
        """
        # Piece should go on the board only if it isn't already there.
        if self.piece is None:
            # Find which square got pressed on the board
            current_square_index = self.squares.children.index(instance)

            # Remove the destination square, place piece there
            piece = Knight()
            self.piece = piece
            self.place_piece_at_index(instance, self.piece, current_square_index)
        else:
            self.square_pressed_piece_on_board(self.piece, instance)

    def square_pressed_piece_on_board(self, piece, instance):
        """ Actions to take when the a square on the board gets pressed and
        the piece is already present. This is a call back method.

        :param piece: Piece on the board.
        :param instance: Instance of the square button pressed.
        :return: None.
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
            self.replace_piece_square(board, piece)
            # Remove the destination square, place piece there
            self.place_piece_at_index(instance, piece, current_square_index)
        return

    def undo_callback(self, *args):
        """ Undo the last movement made by the user. This is a callback method.

        :param args: Arguments passed in by the instance.
        :return: None.
        """
        if self.piece:
            # Can't undo unless moves were made
            if self.move_stack:
                # Replace where the piece was
                self.replace_piece_square_undo(self.piece)

                # Get the square we need to move back to
                prev_move = self.move_stack.pop()
                prev_square = prev_move[0]
                prev_square_index = prev_move[1]

                # Move the piece to the destination square
                # Remove the destination square, place piece there
                self.place_piece_at_index(prev_square, self.piece, prev_square_index)
        else:
            print("Oh ho ho my friend. You forgot to place the piece on the board.")
        return
    #######################################################

    #### Piece placement and square search methods ########
    def place_piece_on_board(self, str_ij, piece):
        """ Place a piece at the ij matrix position on the chess board.

        :param str_ij: A string with a matrix coordinate. Example: '16'.
        :param piece: A chess piece.
        :return: Self.
        """

        # The board has a piece now
        self.piece = piece

        # Square to place the piece on
        i, j = self.str_ij_to_int(str_ij)
        square = self.find_square(i, j)
        self.piece.square = square
        index_of_square = self.squares.children.index(square)

        self.squares.remove_widget(square)
        self.squares.add_widget(piece, index_of_square)

        # Determine which squares the piece can move to on the board
        self.piece.make_move_list(self.squares)

        return self

    def place_piece_at_index(self, square, piece, index):
        """ Take a piece and place it on the square in a board.

        :param square: Destination square for the piece
        :param piece: Piece to place on the board.
        :param index: The position of the square in the children list for the board.
        :return: Grid containing squares and piece of the board.
        """
        # Remove the square occupying the space on board
        self.squares.remove_widget(square)

        # Makes sure piece is associated with the new square
        piece.square = square

        # Place the piece at the destination square
        self.squares.add_widget(piece, index)

        # Recalculate the possible moves for the piece based on the new position
        piece.make_move_list(self.squares)

        return self.squares

    def replace_piece_square_undo(self, piece):
        """ Give a square to the place where the piece originally was.

        :param piece: The chess piece.
        :return: None.
        """
        board = self.squares

        # Where the piece was on the board
        occupied_square_index = board.children.index(piece)
        board.remove_widget(piece)

        # Undo the movement count since the player is going back
        self.move_count -= 1

        # Get the appropriate light or dark color for the square
        # and create a new square
        color = self.color_square(piece.square.position)
        occupied_square = Square(piece.square.position, color)

        # Let the piece move back to this square if necessary
        occupied_square.bind(on_release=self.square_pressed)

        board.add_widget(occupied_square, occupied_square_index)
        return

    def replace_piece_square(self, board, piece):
        """ Give a square to the place where the piece was.

        :param board: Chess board.
        :param piece: Chess piece.
        :return: None.
        """

        # Where the piece was on the board
        piece_square = piece.square
        occupied_square_index = board.children.index(piece)
        board.remove_widget(piece)

        # Get the appropriate light or dark color for the square
        # and create a new square
        color = self.color_square(piece.square.position)
        occupied_square = Square(piece.square.position, color, str(self.move_count))
        self.move_count += 1

        # Give tint to indicate a piece has already been on this square
        dark_blue = [0, 0.30, 1, 0.9]
        occupied_square.background_color = dark_blue

        # In case the user wants to undo
        self.move_stack.append((occupied_square, occupied_square_index))

        # Place a tinted square back on the board
        board.add_widget(occupied_square, occupied_square_index)
        return

    def find_square(self, i, j):
        """ Get the square in ith row, jth column in the board.
        Starting from 1st row

        :param i: Row
        :param j: Column
        :return: Square object if present in children of self.squares.
        """
        for square in self.squares.children:
            # Position encoded from 1th row, 1th column
            position = str(i) + str(j)
            if position == square.position:
                return square
        print("Square not found for combination of i and j")
        return None
    #######################################################