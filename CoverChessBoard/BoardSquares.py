from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from functools import partial
from CoverChessBoard.ChessPieces import *

class Square(Button):

    def __init__(self, ij, color, text = ""):
        # See the coordinates on the board
        # TODO remove coordinates on board
        # --> simply remove text = ij and no coordinates will be seen
        # --> maintain until first version is ready to release
        super().__init__(text = text)
        self.background_color = color

        # Position on the board in matrix notation. Assume i and j both begin at 1.
        self.position = ij
        # Row
        self.i = int(ij[0])
        # Column
        self.j = int(ij[1])

class Board():
    """
    Setup squares as a grid
    """

    def __init__(self, light_color, dark_color, dimension):
        """ Instantiate colors for the board

        :param light_color:
        :param dark_color:
        """
        self.light_color = light_color
        self.dark_color = dark_color

        # Squares given in a GridLayout
        self.squares = self.make_squares(light_color, dark_color, dimension)

        # Assuming only a single piece will ever a be on the squares
        self.piece = None

        # How many movements the player has gone through
        self.move_count = 0

        # Track what movements are made in case the player wants to undo
        self.move_stack = []

    ### ij position methods ###############################

    def str_ij_to_int(self, ij):
        i = int(ij[0])
        j = int(ij[1])
        return i,j

    def move_piece_to_str_ij(self, str_ij, piece,*largs):
        """ Have the program move the piece to an ij position on the board.

        :param str_ij:
        :param board:
        :param piece:
        :param largs:
        :return:
        """
        # Replace the square where the piece originates
        self.replace_piece_square(self.squares, piece)

        # Move the piece to ij position on board
        i, j = self.str_ij_to_int(str_ij)
        destination_square = self.find_square(i, j)
        children = self.squares.children
        index_to_move = children.index(destination_square)
        self.place_piece_at_index(destination_square, piece, index_to_move)

    #######################################################

    ### Square creation methods ###########################

    def color_square(self, position):
        """ Takes the position of a square and gives it the appropriate color
        on the chess board.

        :param position:
        :return:
        """
        i, j = self.str_ij_to_int(position)
        if (i + j) % 2 == 0:
            white = [1, 1, 1, 1]
            color = white
        else:
            mild_green = [0, 0.6,0.29, 1]
            color = mild_green
        return color

    def make_square(self, text, color):
        return Square(text, color)

    def make_squares(self, light_color, dark_color, n):
        """ Create a grid of squares with n by n dimensions

        :param light_color:
        :param dark_color:
        :return:
        """
        grid = GridLayout(cols = n)
        for i in range(0, n):
            for j in range(0, n):
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

    #######################################################

    #### Event handling methods ###########################

    def bind_squares_in_board(self):
        """ Bind button events to squares on the chess board.

        :param board:
        :return:
        """

        for obj in self.squares.children:
            # Only bind the square objects, not the Piece object
            if not isinstance(obj, Piece):
                obj.bind(on_release = partial(self.square_pressed))

    def square_pressed(self, instance):
        """ First event expected from user. Place the piece on the square that got pressed.

        :param piece:
        :param instance:
        :return:
        """
        # Piece should go on the board only if it isn't already there!
        if self.piece is None:
            # Find which square got pressed on the board
            current_square_index = self.squares.children.index(instance)

            # Remove the destination square, place piece there
            # -- NOTE THIS HARDCODES KNIGHT
            piece = Knight()
            self.piece = piece
            self.place_piece_at_index(instance, self.piece, current_square_index)
        else:
            self.square_pressed_piece_on_board(self.piece, instance)

    def square_pressed_piece_on_board(self, piece, instance):
        """ Actions to take when the a square on the board gets pressed and
        the piece is already present.

        :param piece:
        :param instance:
        :return:
        """

        # Find which square got pressed on the board
        board = instance.parent
        current_square_index = board.children.index(instance)

        # Only move the piece if the piece can move to that square
        if instance in piece.possible_moves:
            # If the piece hasn't been pressed, don't move it
            if piece.state == "normal":
                return

            # Remove the piece, place a new square there
            self.replace_piece_square(board, piece)
            # Remove the destination square, place piece there
            self.place_piece_at_index(instance, piece, current_square_index)

    def undo_callback(self, *args):
        if self.piece:
            # Can't undo unless moves were made
            if self.move_stack:
                # Replace where the piece was
                self.replace_piece_square_undo(self.piece)

                # Get the square we need to move back to
                prev_move = self.move_stack.pop()
                prev_square = prev_move[0]
                prev_square_index = prev_move[1]

                # Move the piece to the destination square
                # Remove the destination square, place piece there
                self.place_piece_at_index(prev_square, self.piece, prev_square_index)

        else:
            print("Oh ho ho my friend. You forgot to place the piece on the board.")
    #######################################################

    #### Piece placement and square search methods ########
    def place_piece_on_board(self, str_ij, piece):
        """ Place a piece at the ij matrix position on the chess board.

        :param i:
        :param j:
        :param piece:
        :return:
        """

        # The board has a piece now
        self.piece = piece

        i, j = self.str_ij_to_int(str_ij)

        square = self.find_square(i, j)
        self.piece.square = square
        index_of_square = self.squares.children.index(square)

        self.squares.remove_widget(square)
        self.squares.add_widget(piece, index_of_square)

        # Determine which squares the piece can move to on the board
        self.piece.make_move_list(self.squares)

        return self

    def place_piece_at_index(self, square, piece, index):
        """ Take a piece and place it on the square in a board. Index is the position of the
        square in the children list for the board.

        :param square: Destination square for the piece
        :param piece:
        :param index:
        :param children:
        :return:
        """
        # Remove the square occupying the space on board
        self.squares.remove_widget(square)

        # Makes sure piece is associated with the new square
        piece.square = square

        # Place the piece at the destination square
        self.squares.add_widget(piece, index)

        # Recalculate the possible moves for the piece based on the new position
        piece.make_move_list(self.squares)

        return self.squares

    # Got the movement away from the square
    # -- need to figure out how to get the square we're moving to
    def replace_piece_square_undo(self, piece):
        board = self.squares

        # Where the piece was on the board
        occupied_square_index = board.children.index(piece)
        board.remove_widget(piece)

        # Get the appropriate light or dark color for the square
        # and create a new square
        self.move_count -= 1
        color = self.color_square(piece.square.position)
        occupied_square = Square(piece.square.position, color)

        # Let the piece move back to this square
        occupied_square.bind(on_release=self.square_pressed)

        board.add_widget(occupied_square, occupied_square_index)

    def replace_piece_square(self, board, piece):

        # Where the piece was on the board
        piece_square = piece.square
        occupied_square_index = board.children.index(piece)
        board.remove_widget(piece)

        # Get the appropriate light or dark color for the square
        # and create a new square
        color = self.color_square(piece.square.position)
        occupied_square = Square(piece.square.position, color, str(self.move_count))
        self.move_count += 1

        # Give tint to indicate a piece has already been on this square
        dark_blue = [0, 0.30, 1, 0.9]
        occupied_square.background_color = dark_blue

        # Uncomment to allow moving back to a square the piece
        # has stepped on
        # occupied_square.bind(on_release = self.square_pressed)

        # In case the user wants to undo
        self.move_stack.append([occupied_square, occupied_square_index])

        # Place a tinted square back on the board
        board.add_widget(occupied_square, occupied_square_index)

    def find_square(self, i, j):
        """ Get the square in ith row, jth column in the board.
        Starting from 1st row

        :param i: Row
        :param j: Column
        :return:
        """
        for square in self.squares.children:
            # Position encoded from 1th row, 1th column
            position = str(i) + str(j)
            if position == square.position:
                return square
        print("Square not found for combination of i and j")
        return None
    #######################################################