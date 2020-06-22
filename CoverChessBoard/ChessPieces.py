"""
Images for pieces at https://pixabay.com/illustrations/chess-chess-pieces-shah-mat-pawn-2490568/
"""

from kivy.uix.togglebutton import ToggleButton

class Piece(ToggleButton):

    def __init__(self, piece_name = "", color = [], square = None, possible_moves = []):
        super().__init__()
        self.text = piece_name
        self.background_color = color
        # Where the piece is placed on the board
        self.square = square
        self.possible_moves = possible_moves

    def make_move_list(self, squares):
        """ Make a list of moves for the piece """
        pass

    def diagonal_moves(self, i, j, other_squares, possible_moves, piece_type):
        piece_sum_ij = i + j
        piece_diff_ij = i - j
        for square in other_squares:
            if not isinstance(square, piece_type):
                square_sum_ij = square.i + square.j
                square_diff_ij = square.i - square.j
                if (piece_sum_ij == square_sum_ij) or (piece_diff_ij == square_diff_ij):
                    possible_moves.append(square)

    def row_col_moves(self, other_squares, piece_square, possible_moves, piece_type):
        for square in other_squares:
            if not isinstance(square, piece_type):
                if (piece_square.i == square.i) or (piece_square.j == square.j):
                    possible_moves.append(square)

class Knight(Piece):

    def __init__(self):
        # White, or no tint on piece
        super().__init__(color = [1, 1, 1, 1])
        self.background_normal = "images/knight_up.png"
        self.background_down = "images/knight_down.png"

    def make_move_list(self, squares):
        assert self.square is not None, "The piece isn't on a square yet"

        other_squares = squares.children
        piece_square = self.square
        i = piece_square.i
        j = piece_square.j

        # A knight moves in an "L" shape
        possible_moves = []
        for square in other_squares:
            if not isinstance(square, Knight):
                if (square.j == j - 1) or (square.j == j + 1):
                    if (square.i == i + 2) or (square.i == i - 2):
                        possible_moves.append(square)
                elif (square.i == i + 1) or (square.i == i - 1):
                    if (square.j == j - 2) or (square.j == j + 2):
                        possible_moves.append(square)
        self.possible_moves = possible_moves

class Bishop(Piece):

    def __init__(self):
        super().__init__(color = [1, 1, 1, 1])
        self.background_normal = "images/bishop_up.png"
        self.background_down = "images/bishop_down.png"

    def make_move_list(self, squares):
        assert self.square is not None, "The piece isn't on a square yet"

        other_squares = squares.children
        piece_square = self.square
        i = piece_square.i
        j = piece_square.j

        # A bishop can move down diagonals
        possible_moves = []

        self.diagonal_moves(i, j, other_squares, possible_moves, Bishop)
        self.possible_moves = possible_moves

class King(Piece):
    def __init__(self):
        super().__init__(color = [1, 1, 1, 1])
        self.background_normal = "images/king_up.png"
        self.background_down = "images/king_down.png"

    def make_move_list(self, squares):
        assert self.square is not None, "The piece isn't on a square yet"

        other_squares = squares.children
        piece_square = self.square
        i = piece_square.i
        j = piece_square.j

        # A King can move one space in any direction
        possible_moves = []
        for square in other_squares:
            if not isinstance(square, King):
                # For column after the King
                if square.j == j + 1:
                    if (square.i == i) or (square.i == i - 1) or (square.i == i + 1):
                        possible_moves.append(square)
                # For column of King
                if square.j == j:
                    if (square.i == i - 1) or (square.i == i + 1):
                        possible_moves.append(square)
                # For columb before the King
                if square.j == j - 1:
                    if (square.i == i) or (square.i == i - 1) or (square.i == i + 1):
                        possible_moves.append(square)
        self.possible_moves = possible_moves

class Queen(Piece):
    def __init__(self):
        super().__init__(color = [1, 1, 1, 1])
        self.background_normal = "images/queen_up.png"
        self.background_down = "images/queen_down.png"

    def make_move_list(self, squares):
        assert self.square is not None, "The piece isn't on a square yet"

        other_squares = squares.children
        piece_square = self.square
        i = piece_square.i
        j = piece_square.j

        # A queen moves like a bishop and a rook combined
        possible_moves = []
        self.diagonal_moves(i, j, other_squares, possible_moves, Queen)
        self.row_col_moves(other_squares, piece_square, possible_moves, Queen)

        self.possible_moves = possible_moves

class Pawn(Piece):
    def __init__(self):
        super().__init__(color = [1, 1, 1, 1])
        self.background_normal = "images/pawn_up.png"
        self.background_down = "images/pawn_down.png"

    def make_move_list(self, squares):
        assert self.square is not None, "The piece isn't on a square yet"

        other_squares = squares.children
        piece_square = self.square
        i = piece_square.i
        j = piece_square.j

        # A King can move one space in any direction
        possible_moves = []

        # TODO computationally inefficent, is there a faster way to find the single potential square?
        for square in other_squares:
            if not isinstance(square, Pawn):
                if (square.i == i - 1) and (square.j == j):
                    possible_moves.append(square)

        self.possible_moves = possible_moves

class Rook(Piece):
    def __init__(self):
        super().__init__(color = [1, 1, 1, 1])
        self.background_normal = "images/rook_up.png"
        self.background_down = "images/rook_down.png"

    def make_move_list(self, squares):
        """ What squares can a piece move to, calculate these.

        :return:
        """
        assert self.square is not None, "The piece isn't on a square yet"

        other_squares = squares.children
        piece_square = self.square

        # A rook can move in rows or columns
        possible_moves = []
        self.row_col_moves(other_squares, piece_square, possible_moves, Rook)

        self.possible_moves = possible_moves