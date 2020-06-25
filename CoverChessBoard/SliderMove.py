"""
Interested in making a slider that will move a piece automatically throughout the board.

Ideas:
- Slider obejct in Kivy
- Make a list that has moves, the slider selects positions in the list as it itself moves.
--> List of positions where we want to move the piece,

Research:
- Event, how do you make a button click itself?
Use event or trigger? Do you think?

- How do you hook up a slider to an event, button, action?
"""

from kivy.app import App
from kivy.clock import Clock
from CoverChessBoard.BoardSquares import *
from CoverChessBoard.ChessPieces import *
from functools import partial
import time

class BoardAndPiece(App):

    def str_ij_to_int(self, ij):
        i = int(ij[0])
        j = int(ij[1])
        return i,j

    def place_piece_at_index(self, square, piece, index, children):
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

    def color_square(self, position):
        """ Takes the position of a square and gives it the appropriate color
        on the chess board.

        :param position:
        :return:
        """
        i, j = self.str_ij_to_int(position)
        if (i + j) % 2 == 0:
            white = [1, 1, 1, 1]
            color = white
        else:
            mild_green = [0, 0.6,0.29, 1]
            color = mild_green
        return color

    def square_pressed(self, piece, instance):
        """ Actions to take when the a square on the board gets pressed.

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
            self.replace_piece_square(board, piece)
            # Remove the destination square, place piece there
            self.place_piece_at_index(instance, piece, current_square_index, board)

    def replace_piece_square(self, board, piece):

        # Where the piece was on the board
        occupied_square_index = board.children.index(piece)
        board.remove_widget(piece)

        # Get the appropriate light or dark color for the square
        # and create a new square
        color = self.color_square(piece.square.position)
        occupied_square = Square(piece.square.position, color)

        # Give tint to indicate a piece has already been on this square
        dark_blue = [0, 0.30, 1, 0.9]
        occupied_square.background_color = dark_blue

        # Uncomment to allow moving back to a square the piece
        # has stepped on
        # occupied_square.bind(on_release = self.square_pressed)

        # Place a tinted square back on the board
        board.add_widget(occupied_square, occupied_square_index)

    def bind_squares_in_board(self, board):
        """ Bind button events to squares on the chess board.

        :param board:
        :return:
        """

        for obj in board.squares.children:
            # Only bind the square objects, not the Piece object
            if not isinstance(obj, Piece):
                obj.bind(on_release = partial(self.square_pressed, board.piece))

    def move_piece_to_str_ij(self, str_ij, board, piece, *largs):
        """ Have the program move the piece to an ij position on the board.

        :param str_ij:
        :param board:
        :param piece:
        :param largs:
        :return:
        """
        # Replace the square where the piece originates
        self.replace_piece_square(board.squares, piece)

        # Move the piece to ij position on board
        i, j = self.str_ij_to_int(str_ij)
        destination_square = board.find_square(i, j)
        children = board.squares
        index_to_move = children.index(destination_square)
        self.place_piece_at_index(destination_square, piece, index_to_move, children)

    def make_board(self):
        white = [1, 1, 1, 1]
        mild_green = [0, 0.6, 0.29, 1]
        dim = 8
        board = SquaresLayout(white, mild_green, dim)
        return board

    def build(self):
        board = self.make_board()

        piece = King()
        board = board.place_piece_on_board(1, 1, piece)
        self.bind_squares_in_board(board)

        #move_list = piece.column_algorithmic_solution
        #seconds = 1
        #for move in move_list:
         #   Clock.schedule_once(partial(self.move_piece_to_str_ij, move, board, piece), seconds)
          #  seconds += 0.1

        return board.squares

game = BoardAndPiece()
game.run()