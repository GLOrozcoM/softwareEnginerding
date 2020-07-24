"""
This module was built to encapsulate chess pieces and their movement.
Although the program only requires a definition for the knight, other
viable tour pieces are included for another eventual program with all pieces.

Images for pieces at https://pixabay.com/vectors/chess-pieces-set-symbols-game-26774/
"""

from kivy.uix.togglebutton import ToggleButton


class Piece(ToggleButton):

    def __init__(self, piece_name="", color=[], square=None, possible_moves=[]):
        super().__init__()
        self.text = piece_name

        # Tint the piece receives
        self.background_color = color

        # Where the piece is placed on the board
        self.square = square
        self.possible_moves = possible_moves

    def make_move_list(self, squares):
        """Abstract method. Make a list of moves for the piece"""
        pass

    def diagonal_moves(self, i, j, other_squares, possible_moves, piece_type):
        """ Modify possible_moves list to contain the moves this piece can go to.

        :param i: Row.
        :param j: Column.
        :param other_squares: Other squares on the chess board.
        :param possible_moves: Legal chess moves for the piece.
        :param piece_type: Bishop or Queen (diagonal movers).
        :return: None
        """
        piece_sum_ij = i + j
        piece_diff_ij = i - j
        for square in other_squares:
            if not isinstance(square, piece_type):
                square_sum_ij = square.i + square.j
                square_diff_ij = square.i - square.j
                if (piece_sum_ij == square_sum_ij) or (piece_diff_ij == square_diff_ij):
                    possible_moves.append(square)

    def row_col_moves(self, other_squares, piece_square, possible_moves, piece_type):
        """ Give possible_moves the row or column moves for the piece.

        :param other_squares: Other squares on the chess board.
        :param piece_square: Square this piece is on.
        :param possible_moves: Legal chess moves for the piece.
        :param piece_type: Rook or Queen (row or column movers).
        :return:
        """
        for square in other_squares:
            if not isinstance(square, piece_type):
                if (piece_square.i == square.i) or (piece_square.j == square.j):
                    possible_moves.append(square)


class Knight(Piece):

    def __init__(self):
        # White, or no tint on piece
        super().__init__(color=[1, 1, 1, 1])
        self.background_normal = "../images/SimpleSet/knight_up.png"
        self.background_down = "../images/SimpleSet/knight_down.png"

    def make_move_list(self, squares):
        """ Create legal chess moves for the Knight.

        :param squares: Chess board square objects.
        :return: None
        """
        assert self.square is not None, "The piece isn't on a square yet"

        other_squares = squares.children
        piece_square = self.square
        i = piece_square.i
        j = piece_square.j

        possible_moves = []
        for square in other_squares:
            if not isinstance(square, Knight):
                # A knight moves in an "L" shape
                # -- two rows and one column, or two columns and one row
                if (square.j == j - 1) or (square.j == j + 1):
                    if (square.i == i + 2) or (square.i == i - 2):
                        possible_moves.append(square)
                elif (square.i == i + 1) or (square.i == i - 1):
                    if (square.j == j - 2) or (square.j == j + 2):
                        possible_moves.append(square)
        self.possible_moves = possible_moves
        return


class Bishop(Piece):

    def __init__(self):
        super().__init__(color=[1, 1, 1, 1])
        self.background_normal = "../images/SimpleSet/bishop_up.png"
        self.background_down = "../images/SimpleSet/bishop_down.png"

    def make_move_list(self, squares):
        """

        :param squares: Chess board squares.
        :return: None
        """
        assert self.square is not None, "The piece isn't on a square yet"

        other_squares = squares.children
        piece_square = self.square
        i = piece_square.i
        j = piece_square.j

        possible_moves = []

        self.diagonal_moves(i, j, other_squares, possible_moves, Bishop)
        self.possible_moves = possible_moves
        return


class King(Piece):

    def __init__(self):
        super().__init__(color=[1, 1, 1, 1])
        self.background_normal = "../images/SimpleSet/king_up.png"
        self.background_down = "../images/SimpleSet/king_down.png"

    def make_move_list(self, squares):
        """ Create legal chess moves for the King.

        :param squares: Chess board squares.
        :return: None
        """
        assert self.square is not None, "The piece isn't on a square yet"

        other_squares = squares.children
        piece_square = self.square
        i = piece_square.i
        j = piece_square.j

        possible_moves = []
        for square in other_squares:
            if not isinstance(square, King):
                # A King can move one space in any direction
                # -- for column after the King
                if square.j == j + 1:
                    if (square.i == i) or (square.i == i - 1) or (square.i == i + 1):
                        possible_moves.append(square)
                # -- for column of King
                if square.j == j:
                    if (square.i == i - 1) or (square.i == i + 1):
                        possible_moves.append(square)
                # -- for column before the King
                if square.j == j - 1:
                    if (square.i == i) or (square.i == i - 1) or (square.i == i + 1):
                        possible_moves.append(square)
        self.possible_moves = possible_moves
        return


class Queen(Piece):

    def __init__(self):
        super().__init__(color=[1, 1, 1, 1])
        self.background_normal = "../images/SimpleSet/queen_up.png"
        self.background_down = "../images/SimpleSet/queen_down.png"

    def make_move_list(self, squares):
        """ Create legal chess moves for queen.

        :param squares: Chess board squares.
        :return: None.
        """
        assert self.square is not None, "The piece isn't on a square yet"

        other_squares = squares.children
        piece_square = self.square
        i = piece_square.i
        j = piece_square.j

        possible_moves = []

        # A queen moves like the bishop and rook combined.
        self.diagonal_moves(i, j, other_squares, possible_moves, Queen)
        self.row_col_moves(other_squares, piece_square, possible_moves, Queen)
        self.possible_moves = possible_moves
        return


class Pawn(Piece):

    def __init__(self):
        super().__init__(color=[1, 1, 1, 1])
        self.background_normal = "../images/SimpleSet/pawn_up.png"
        self.background_down = "../images/SimpleSet/pawn_down.png"

    def make_move_list(self, squares):
        """ Create legal chess moves for the pawn.

        :param squares: Chess board squares.
        :return: None.
        """
        assert self.square is not None, "The piece isn't on a square yet"

        other_squares = squares.children
        piece_square = self.square
        i = piece_square.i
        j = piece_square.j

        possible_moves = []

        for square in other_squares:
            if not isinstance(square, Pawn):
                # Stick to the same column, one row up
                if (square.i == i - 1) and (square.j == j):
                    possible_moves.append(square)

        self.possible_moves = possible_moves
        return


class Rook(Piece):

    def __init__(self):
        super().__init__(color=[1, 1, 1, 1])
        self.background_normal = "../images/SimpleSet/rook_up.png"
        self.background_down = "../images/SimpleSet/rook_down.png"

    def make_move_list(self, squares):
        """ Create legal chess moves for the rook.

        :return: None.
        """
        assert self.square is not None, "The piece isn't on a square yet"

        other_squares = squares.children
        piece_square = self.square

        possible_moves = []
        self.row_col_moves(other_squares, piece_square, possible_moves, Rook)

        self.possible_moves = possible_moves
        return
