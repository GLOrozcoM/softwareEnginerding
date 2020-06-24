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

    def string_coordinate_to_number(self, ij):
        i = int(ij[0])
        j = int(ij[1])
        return i,j

    def place_piece_at_index(self, square, piece, index, children):
        """ Children list index

        :param index:
        :return:
        """
        children.remove_widget(square)
        piece.square = square
        children.add_widget(piece, index)

        # Recalculate the possible moves for the piece
        piece.make_move_list(children)

        return children

    def color_square(self, position):

        i, j = self.string_coordinate_to_number(position)
        if (i + j) % 2 == 0:
            color = [1, 1, 1, 1]
        else:
            color = [0, 0.6,0.29, 1]
        return color

    def square_pressed(self, instance):
        board = instance.parent
        current_square_index = board.children.index(instance)

        # TODO find faster way to select a piece from the board
        # TODO "piece" could become a hanging variable
        # --> a way to pass the board object and then immediately select the piece.
        # --> find out how to use lambda and partial

        # Got the piece
        for square in board.children:
            if isinstance(square, Piece):
                piece = square

        # Make sure the square that got pressed is in the list of possible moves for the piece
        if instance in piece.possible_moves:
            if piece.state == "normal":
            # Nothing occurs since the piece hasn't been selected
                return

            # Remove the piece, place a new square there
            self.replace_piece_square(board, piece)
            # Remove the old square, place piece there
            self.place_piece_at_index(instance, piece, current_square_index, board)

    def replace_piece_square(self, board, piece):
        occupied_square_index = board.children.index(piece)
        board.remove_widget(piece)

        color = self.color_square(piece.square.position)
        occupied_square = Square(piece.square.position, color)
        occupied_square.bind(on_release=self.square_pressed)

        board.add_widget(occupied_square, occupied_square_index)

    def bind_squares_in_board(self, board):
        for square in board.squares.children:
            if not isinstance(square, Piece):
                square.bind(on_release = self.square_pressed)

    def move_piece_through_move_list(self, str_coords, board, piece, *largs):
        print('My callback is called')

        # Replace the square of the piece
        # -- where we come from
        self.replace_piece_square(board.squares, piece)

        # Move the piece
        # -- where we want to move
        i, j = self.string_coordinate_to_number(str_coords)
        destination_square = board.find_square(i, j)
        children = board.squares
        index_to_move = board.squares.children.index(destination_square)
        self.place_piece_at_index(destination_square, piece, index_to_move, children)

    def build(self):
        white = [1, 1, 1, 1]
        mild_green = [0, 0.6, 0.29, 1]
        board = SquaresLayout(white, mild_green)

        piece = Queen()
        board = board.place_piece_on_board(1, 1, piece)
        self.bind_squares_in_board(board)

        move_list = ["18", "88", "11", "55", "88"]
        seconds = 1
        for move in move_list:
            Clock.schedule_once(partial(self.move_piece_through_move_list, move, board, piece), seconds)
            seconds += 1

        return board.squares


g = BoardAndPiece()
g.run()