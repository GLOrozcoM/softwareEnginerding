"""
Experimenting with images for pieces, simpler encapsulated board construction.
"""

from kivy.app import App
from CoverChessBoard.BoardSquares import *
from CoverChessBoard.src.ChessPieces import *


class BoardAndPiece(App):

    def setup_board(self):
        white = [1, 1, 1, 1]
        mild_green = [0, 0.6, 0.29, 1]
        dim = 8
        board = Board(white, mild_green, dim)
        return board

## Place to test solution path
    def build(self):
        board = self.setup_board()

        piece = Knight()
        start = "55"
        board = board.place_piece_on_board(start, piece)
        board.bind_squares_in_board()

        return board.squares

game = BoardAndPiece()
game.run()