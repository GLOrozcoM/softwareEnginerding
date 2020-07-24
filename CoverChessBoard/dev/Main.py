"""
Develop application driver.
"""
from kivy.app import App
from CoverChessBoard.dev.MenuScreen import *
from CoverChessBoard.dev.WelcomeScreen import *
from CoverChessBoard.dev.ComputerBoardScreen import *
from CoverChessBoard.dev.PlayerBoardScreen import *
from CoverChessBoard.dev.ExplanationScreen import *
from kivy.uix.screenmanager import ScreenManager


class ConquerChessBoard(App):

    def build(self):
        sm = ScreenManager()

        sm.add_widget(setup_welcome_screen(sm))
        sm.add_widget(setup_menuscreen(sm))
        sm.add_widget(setup_computer_board_screen(sm))
        sm.add_widget(setup_player_screen(sm))
        sm.add_widget(setup_explanation_screen(sm))

        return sm


app = ConquerChessBoard()
app.run()