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

def generate_vertical_buttons( ):
    v_layout = BoxLayout(orientation = 'vertical')
    for i in range(0, 8):
        v_layout.add_widget( Button(text = str(i)) )
    return v_layout

def fill_horizontal_slots():
    h_layout = BoxLayout(orientation = 'horizontal')
    for i in range(0, 8):
        vertical_buttons = generate_vertical_buttons()
        h_layout.add_widget( vertical_buttons )
    return h_layout

class Board(App):

    def build(self):

        full_board = fill_horizontal_slots()

        return full_board

Board().run()

