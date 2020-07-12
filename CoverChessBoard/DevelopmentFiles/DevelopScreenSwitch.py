"""

Develop familiarity with how to switch screens

"""

from kivy.app import App
from CoverChessBoard.BoardSquares import *
from CoverChessBoard.ChessPieces import *
from functools import partial

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from kivy.uix.screenmanager import ScreenManager, Screen

# Create the manager
sm = ScreenManager()

def switch_to_screen_two(screen_manager, *args):
    screen_manager.current = 'screen two'

def switch_to_screen_one(screen_manager, *args):
    screen_manager.current = 'screen one'

go_screen_two = Button(text = "Go to screen two")
go_screen_two.bind(on_release = partial(switch_to_screen_two, sm))
screen_one = Screen(name = "screen one")
screen_one.add_widget(go_screen_two)

go_screen_one = Button(text = "Go to screen one")
go_screen_one.bind(on_release = partial(switch_to_screen_one, sm))
screen_two = Screen(name = "screen two")
screen_two.add_widget(go_screen_one)

sm.add_widget(screen_one)
sm.add_widget(screen_two)

sm.current = "screen one"


class TestApp(App):

    def build(self):
        return sm

app = TestApp()
app.run()