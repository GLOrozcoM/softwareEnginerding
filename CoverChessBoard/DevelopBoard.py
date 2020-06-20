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

class GridBoard(App):

    def build(self):
        white = [1, 1, 1, 1]
        mild_green = [0, 0.6, 0.29, 1]
        board = ChessBoard(white, mild_green)

        piece = Piece("Piece", [1, 0, 0, 1])

        board = board.place_piece(1, 1, piece)

        return board.squares


board = GridBoard()
board.run()