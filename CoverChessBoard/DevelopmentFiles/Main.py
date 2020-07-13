"""

Develop application driver.

"""

from CoverChessBoard.DevelopmentFiles.MenuScreen import *
from CoverChessBoard.DevelopmentFiles.WelcomeScreen import *
from kivy.uix.screenmanager import ScreenManager, Screen
from functools import partial

class ConquerChessBoard(App):

    def build(self):
        sm = ScreenManager()

        welcome_layout = create_welcome_layout(sm)
        menu_layout = create_menu_layout()

        welcome_screen = Screen(name="welcome_screen")
        menu_screen = Screen(name="menu_screen")

        welcome_screen.add_widget(welcome_layout)
        menu_screen.add_widget(menu_layout)

        sm.add_widget(welcome_screen)
        sm.add_widget(menu_screen)

        return sm




app = ConquerChessBoard()
app.run()