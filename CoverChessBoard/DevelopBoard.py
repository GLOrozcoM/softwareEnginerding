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
from CoverChessBoard.ChessObjects import ChessBoard
from CoverChessBoard.ChessObjects import Piece
from CoverChessBoard.ChessObjects import Square

# TODO remove square from board function

class GridBoard(App):

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

        return children

    def color_square(self, position):

        i, j = self.string_coordinate_to_number(position)
        if (i + j) % 2 == 0:
            color = [1, 1, 1, 1]
        else:
            color = [0, 0.6,0.29, 1]
        return color

    def square_pressed(self, instance):
        print("Pressed!")
        board = instance.parent
        index_of_curr_square = board.children.index(instance)
        for child in board.children:
            if isinstance(child, Piece):
                piece = child
                index_occupied_square = board.children.index(piece)
                board.remove_widget(piece)

                color = self.color_square(piece.square.position)
                occupied_square = Square(piece.square.position, color)
                occupied_square.bind(on_release = self.square_pressed)
                board.add_widget(occupied_square, index_occupied_square)

                # Remove the old square, place new piece there
        self.place_piece_at_index(instance, piece, index_of_curr_square, board)

        # Redo bindings

        return None

    def bind_squares_in_board(self, board):
        for child in board.squares.children:
            if not isinstance(child, Piece):
                child.bind(on_release = self.square_pressed)

    def build(self):
        white = [1, 1, 1, 1]
        mild_green = [0, 0.6, 0.29, 1]
        board = ChessBoard(white, mild_green)

        piece = Piece("Piece", [1, 0, 0, 1])
        board = board.place_piece(1, 1, piece)


        self.bind_squares_in_board(board)

        return board.squares


board = GridBoard()
board.run()