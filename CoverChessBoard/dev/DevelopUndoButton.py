from kivy.uix.button import Button
from CoverChessBoard.BoardSquares import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.app import App

def make_board():
    white = [1, 1, 1, 1]
    mild_green = [0, 0.6, 0.29, 1]
    dim = 8
    board = Board(white, mild_green, dim)
    return board

def setup_board():
    board = make_board()
    piece = Knight()
    board.place_piece_on_board("11", piece)
    board.bind_squares_in_board()
    return board

def create_player_board_layout():

    ## TODO place a small paragraph talking to the user
    ## TODO place a back button to go to previous screen
    layout = BoxLayout(orientation='horizontal')

    board = setup_board()

    undo_btn = Button(text="Undo",
                      size_hint=(0.2,1),
                      background_normal='',
                      background_down='',
                      background_color=(0,0,0.14,1),
                      color=(1, 1, 1, 0.7))
    undo_btn.bind(on_release=board.undo_callback)

    layout.add_widget(board.squares)
    layout.add_widget(undo_btn)

    return layout

#### Testing in this file
class UndoScreen(App):

    def build(self):
        layout = create_player_board_layout()

        return layout

undo = UndoScreen()
undo.run()