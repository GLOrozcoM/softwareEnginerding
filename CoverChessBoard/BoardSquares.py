from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class Square(Button):

    def __init__(self, ij, color):
        super().__init__(text = ij)
        self.background_color = color
        # Position on the board in matrix notation
        # - Starting from 1th row, 1st column
        self.position = ij
        # Row
        self.i = int(ij[0])
        # Column
        self.j = int(ij[1])

class SquaresLayout():
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

        # Squares given in a GridLayout
        self.squares = self.make_squares(light_color, dark_color)

        # Assuming only a single piece will ever a be on the squares
        self.piece = None

    def piece_starting_point(self, i, j, piece):
        self.piece = piece

        square = self.find_square(i, j)
        self.piece.square = square
        index_of_square = self.squares.children.index(square)

        self.squares.remove_widget(square)
        self.squares.add_widget(piece, index_of_square)

        # Determine which squares the piece can move to on the board
        self.piece.make_move_list(self.squares)

        return self

    def make_square(self, text, color):
        square = Square(text, color)
        return square

    def make_squares(self, light_color, dark_color):
        grid = GridLayout(cols = 8)
        for i in range(0, 8):
            for j in range(0, 8):
                sum = i + j
                if (sum % 2) == 0:
                    text = str(i + 1) + str(j + 1)
                    square = self.make_square(text, light_color)
                    grid.add_widget(square)
                else:
                    text = str(i + 1) + str(j + 1)
                    square = self.make_square(text, dark_color)
                    grid.add_widget(square)
        return grid

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

