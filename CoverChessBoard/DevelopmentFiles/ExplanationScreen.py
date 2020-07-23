"""
This module encapsulates the explanation screen for the user.
-- what is the whole process about?
"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.colorpicker import Color
from kivy.graphics import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from CoverChessBoard.DevelopmentFiles.FooterButtons import *

def create_explanation_layout(screen_manager):
    layout = BoxLayout(orientation='vertical')
    # Give background image to layout
    with layout.canvas.before:
        Color(0, 0, 0.14, 1)
        rect = Rectangle(size=(1000, 1000),
                         pos=layout.pos)

    par_one = create_paragraph_one()
    back_btn = create_back_button(screen_manager)
    back_btn.size_hint=(1, 0.2)

    layout.add_widget(par_one)
    layout.add_widget(back_btn)
    return layout

def create_paragraph_one():
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

def setup_explanation_screen(screen_manager):

    explanation_screen = Screen(name = "explanation_screen")
    layout = create_explanation_layout(screen_manager)
    explanation_screen.add_widget(layout)

    return explanation_screen