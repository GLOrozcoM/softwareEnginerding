"""
This module encapsulates the explanation screen for the user.
-- what is the whole program about?
"""
from kivy.uix.label import Label
from kivy.uix.colorpicker import Color
from kivy.graphics import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from CoverChessBoard.src.GUI.NavigationButtons import *


def create_paragraph():
    """ Make a label containing text for the explanation screen.

    :return: A label containing explanation text.
    """
    paragraph = Label(
        text="""This program intends to replicate the problem of covering every chess square on a chess board \n
             while only visiting each square once. \n\n
            For most pieces, solving this problem is a piece of cake. A rook can just move file by file or row by row.\n
            A king can inch its way successively through the entire board, and the queen can use the rook’s strategy because\n
            they share movement styles. The bishop has no solution since it must stay on one colored diagonals, and \n
            the pawn simply reduces to the other cases.\n\n
            The knight offers a different story. It only moves in an L shape - either two rows and one column over, or \n
            two columns and one row over. This means a knight won’t be sweeping over squares in the board so \n
            determining the right way to cover the board with a knight is challenging.\n\n
            Use this program to try and solve the knight’s tour yourself or have the computer demonstrate a solution.""",
        color=(1, 1, 1, 0.7),
        halign='justify')
    return paragraph


def create_explanation_layout(screen_manager):
    """ Create the layout to contain the text.

    :param screen_manager: The manager for screens in the application.
    :return: A BoxLayout containing the text for the explanation screen.
    """
    layout = BoxLayout(orientation='vertical')
    # Give background image to layout
    with layout.canvas.before:
        Color(0, 0, 0.14, 1)
        rect = Rectangle(size=(5000, 5000),
                         pos=layout.pos)

    paragraph = create_paragraph()
    back_btn = create_back_button(screen_manager)
    # Make the button take up entire width, but only 20% of height
    back_btn.size_hint = (1, 0.2)

    layout.add_widget(paragraph)
    layout.add_widget(back_btn)
    return layout


def setup_explanation_screen(screen_manager):
    """ Make a screen containing an explanation for the program.

    :param screen_manager: The manager for screens in the application.
    :return: A screen containing an explanation for the program.
    """
    explanation_screen = Screen(name="explanation_screen")
    layout = create_explanation_layout(screen_manager)
    explanation_screen.add_widget(layout)
    return explanation_screen