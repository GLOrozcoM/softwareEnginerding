"""

Develop application driver.

"""
from kivy.app import App
from CoverChessBoard.DevelopmentFiles.MenuScreen import *
from CoverChessBoard.DevelopmentFiles.WelcomeScreen import *
from CoverChessBoard.DevelopmentFiles.ComputerBoard import *
from CoverChessBoard.DevelopmentFiles.PlayerBoard import *
from kivy.uix.screenmanager import ScreenManager, Screen

class ConquerChessBoard(App):

    def build(self):
        sm = ScreenManager()

        welcome_layout = create_welcome_layout(sm)
        menu_layout = create_menu_layout(sm)
        player_board_layout = create_player_board_layout()

        welcome_screen = Screen(name="welcome_screen")
        menu_screen = Screen(name="menu_screen")
        player_board_screen = Screen(name="player_board_screen")

        welcome_screen.add_widget(welcome_layout)
        menu_screen.add_widget(menu_layout)
        player_board_screen.add_widget(player_board_layout)

        sm.add_widget(welcome_screen)
        sm.add_widget(menu_screen)
        sm.add_widget(set_up_computer_board_screen())
        sm.add_widget(player_board_screen)

        return sm




app = ConquerChessBoard()
app.run()