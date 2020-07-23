"""

Develop application driver.

"""
from kivy.app import App
from CoverChessBoard.DevelopmentFiles.MenuScreen import *
from CoverChessBoard.DevelopmentFiles.WelcomeScreen import *
from CoverChessBoard.DevelopmentFiles.ComputerBoardScreen import *
from CoverChessBoard.DevelopmentFiles.PlayerBoardScreen import *
from kivy.uix.screenmanager import ScreenManager

class ConquerChessBoard(App):

    def build(self):
        sm = ScreenManager()

        sm.add_widget(setup_welcome_screen(sm))
        sm.add_widget(setup_menuscreen(sm))
        sm.add_widget(setup_computer_board_screen(sm))
        sm.add_widget(setup_player_screen(sm))

        return sm

app = ConquerChessBoard()
app.run()