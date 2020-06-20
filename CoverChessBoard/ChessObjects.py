from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton

class Square(Button):

    def __init__(self, text, color):
        super().__init__(text = text)
        self.background_color = color
        # Position on the board in matrix notation
        # - Starting from 0th row
        self.position = text



class Piece(ToggleButton):

    def __init__(self, piece_name, color):
        super().__init__()
        self.text = piece_name
        self.background_color = color

    def print_state(self, instance, state_value):
        if state_value == 'normal':
            print("the state value is normal")
        else:
            print("the state value is down")

class ChessBoard():
    """
    Setup squares as a grid
    """

    def __init__(self, light_color, dark_color):
        """ Instantiate colors for the board

        :param light_color:
        :param dark_color:
        """
        self.light_color = light_color
        self.dark_color = dark_color
        self.squares = self.make_board(light_color, dark_color)

        # Assuming only a single piece will ever a be on the board
        self.piece = None

    def place_piece(self, i, j, piece):
        self.piece = piece

        square = self.find_square(i, j)
        index_of_square = self.squares.children.index(square)

        self.squares.remove_widget(square)
        self.squares.add_widget(piece, index_of_square)

        return self

    def make_square(self, text, color):
        return Square(text, color)

    def make_board(self, light_color, dark_color):
        board = GridLayout(cols=8)
        for i in range(0, 8):
            for j in range(0, 8):
                sum = i + j
                if (sum % 2) == 0:
                    text = str(i + 1) + str(j + 1)
                    square = self.make_square(text, light_color)
                    board.add_widget(square)
                else:
                    text = str(i + 1) + str(j + 1)
                    square = self.make_square(text, dark_color)
                    board.add_widget(square)
        return board

    def find_square(self, i, j):
        """ Get the square in ith row, jth column in the board.
        Starting from 1st row

        :param i: Row
        :param j: Column
        :return:
        """

        for square in self.squares.children:
            # Position encoded from 0th row
            position = str(i) + str(j)
            if position == square.position:
                return square
        print("Invalid entry combo for i and j")
        return None

