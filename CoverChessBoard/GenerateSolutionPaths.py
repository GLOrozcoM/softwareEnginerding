"""

Note that this will take a while to run. Also, the file produced will
be 59.63 megabytes.

"""

from CoverChessBoard.Backtracker import *
from CoverChessBoard.Warnsdorff import *

# Set up
matrix = make_n_matrix(8)
board = matrix_to_graph(matrix)
add_movement_edges(board, matrix)

# Create solutions for every square on board
n = len(matrix)
for i in range(0, n):
    for j in range(0, n):
        starting_point = [matrix[i][j]]
        backtracker(board, starting_point)

print("Finished")