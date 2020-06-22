"""
Make a piece object that will interact with the board.

Ideas:
-> Make a child class of Button, that willl have a click status attribute.
As the attribute changes, so will its ability to interact with the rest of the board.
Let the board be "aware" of a piece by having a piece attribute and seeing if it has
been clicked.
-> Explore bindings.

"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from CoverChessBoard.BoardSquares import SquaresLayout

"""
Right at press: on_press
Right after release: on_release
Abled or disabled (state): state
"""

class Piece(ToggleButton):

    def __init__(self, piece_name):
        super().__init__()
        self.text = piece_name

    def print_state(self, instance, state_value):
        if state_value == 'normal':
            print("the state value is normal")
        else:
            print("the state value is down")

class Test(App):

    def build(self):

        btn = Piece('Piece')
        btn.bind(state = btn.print_state)

        return btn

the_piece = Test()
the_piece.run()