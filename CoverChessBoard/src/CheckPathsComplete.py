"""
Process the paths found after running Warnsdorff and backtracking algorithm.

Primary goal: confirm that a path solution exists for every square in an 8 by 8 board.

File contains 154888 records so it can take a while to process.

N solution
-> Create list with matrix coordinates (one dimensional vector).
-> Check the first move in each path. If the move is in the matrix,
pop it.
-> Continue until the end of file or when the vector is empty (we saw every coordinate in the matrix).

This is simple to understand, but expensive. We end up checking every line up until the 88 line
when we could simply jump over a few solutions.

Log N solution
-> Create list with matrix coordinates (one dimensional vector).
-> Conduct a binary search for a path based on each entry in the vector.
-> If a path isn't found, break and output for which coordinate a path didn't exist.
-> If the loop ends without breaking, a path existed for each square.
"""
from CoverChessBoard.src.FindSolutionPath import *


def generate_squares():
    """ Make a list of matrix coordinates. (Start at 11 go to 88)

    :return: A list of all matrix coordinates on an 8 by 8 chess board.
    """
    squares = []
    for i in range(1, 9):
        for j in range(1, 9):
            coord = str(i) + str(j)
            squares.append(coord)
    return squares


def perform_check(file_name):
    """ Check if all squares in the chess board have a solution path.

    :param file_name: File to look for the solutions in.
    :return: None
    """
    squares = generate_squares()

    n = len(squares)
    for i in range(0, n):
        path_start = squares[i]
        print("Checking path for {}.".format(path_start))
        path = get_path(path_start, file_name)
        if path is None:
            print("Path for {} does not exist.".format(path_start))
            return

    print("Reached the end of the check successfully.")
    return


if __name__ == "__main__":
    print("Knight's tour check")
    knight_tour = "../SolutionPaths/knight_tour.txt"
    perform_check(knight_tour)
    print("Knight's tour check ended")