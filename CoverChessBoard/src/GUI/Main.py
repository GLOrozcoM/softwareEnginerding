"""
Application driver.
"""
from kivy.app import App
from CoverChessBoard.src.GUI.MenuScreen import *
from CoverChessBoard.src.GUI.WelcomeScreen import *
from CoverChessBoard.src.GUI.ComputerBoardScreen import *
from CoverChessBoard.src.GUI.PlayerBoardScreen import *
from CoverChessBoard.src.GUI.ExplanationScreen import *
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

if __name__ == "__main__":
    app = ConquerChessBoard()
    app.run()