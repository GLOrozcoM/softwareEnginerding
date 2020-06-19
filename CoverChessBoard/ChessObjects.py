"""
Prototype class for chess board to use
"""

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class ChessBoard():

    def __init__(self, light_color, dark_color):
        """ Instantiate colors for the board

        :param light_color:
        :param dark_color:
        """
        self.light_color = light_color
        self.dark_color = dark_color
        self.squares = self.fill_rows()

    def make_square(self, column, square_color):
        """ Create a single chess square. Square is a button so user can press it and make moves.

        :param column: Column in a chess board the square gets placed in
        :param square_color: Color of the square
        :return: None
        """
        column.add_widget(Button(background_normal='',
                                 background_color=square_color))

    def add_squares_to_column(self, column, color_one, color_two):
        """

        :param column:
        :param color_one:
        :param color_two:
        :return:
        """
        for i in range(0, 8):
            if (i % 2) == 0:
                self.make_square(column, color_one)
            else:
                self.make_square(column, color_two)

    def make_column(self, parity):
        """

        :param parity:
        :return:
        """
        column = BoxLayout(orientation='vertical')
        # A column in an odd number must start with with light color and end in dark color
        if parity == 'odd':
            self.add_squares_to_column(column, self.dark_color, self.light_color)
        # A column in an even number must start with dark color and end in light color
        else:
            self.add_squares_to_column(column, self.light_color, self.dark_color)
        return column

    def add_column_to_row(self, row, parity):
        """

        :param row:
        :param parity:
        :return:
        """
        vertical_buttons = self.make_column(parity)
        row.add_widget(vertical_buttons)

    def fill_rows(self):
        """

        :return:
        """
        rows = BoxLayout(orientation='horizontal')
        for i in range(0, 8):
            if (i % 2) != 0:
                self.add_column_to_row(rows, 'odd')
            else:
                self.add_column_to_row(rows, 'even')
        return rows
