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
from CoverChessBoard.BoardSquares import *
from CoverChessBoard.ChessPieces import *

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

    def build(self):
        white = [1, 1, 1, 1]
        mild_green = [0, 0.6, 0.29, 1]
        board = SquaresLayout(white, mild_green)

        p = Knight()
        board = board.piece_starting_point(7, 8, p)

        self.bind_squares_in_board(board)

        return board.squares


g = BoardAndPiece()
g.run()