"""

Develop application driver.

"""
from kivy.app import App
from CoverChessBoard.DevelopmentFiles.MenuScreen import *
from CoverChessBoard.DevelopmentFiles.WelcomeScreen import *
from CoverChessBoard.DevelopmentFiles.ChooseSquareScreen import *
from kivy.uix.screenmanager import ScreenManager, Screen

class ConquerChessBoard(App):

    def build(self):
        sm = ScreenManager()

        welcome_layout = create_welcome_layout(sm)
        menu_layout = create_menu_layout(sm)
        choose_square_layout = create_choose_square_layout(sm)

        welcome_screen = Screen(name="welcome_screen")
        menu_screen = Screen(name="menu_screen")
        choose_square_screen = Screen(name="choose_square_screen")

        welcome_screen.add_widget(welcome_layout)
        menu_screen.add_widget(menu_layout)
        choose_square_screen.add_widget(choose_square_layout)

        sm.add_widget(welcome_screen)
        sm.add_widget(menu_screen)
        sm.add_widget(choose_square_screen)
        return sm




app = ConquerChessBoard()
app.run()