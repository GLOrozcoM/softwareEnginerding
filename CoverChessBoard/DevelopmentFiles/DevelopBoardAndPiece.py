"""

Render the piece on the board.
-> Try replacing a button in the matrix with the a piece object.

"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from CoverChessBoard.BoardSquares import Board

class Board(App):

    def build(self):
        white = [1, 1, 1, 1]
        mild_green = [0, 0.6, 0.29, 1]
        chess_board = Board(white, mild_green)

        # REmove one button_to_add from [0,0] in matrix
        # --> Children one columns, children two buttons



        button_to_remove = chess_board.squares.children[0].children[0]
        chess_board.squares.children[0].remove_widget(button_to_remove)

        piece_color =  mild_green
        button_to_add = Button(background_color=piece_color)
        chess_board.squares.children[0].add_widget(button_to_add)

        print(chess_board.squares.children[0].children[0])


        return chess_board.squares


the_board = Board()
the_board.run()