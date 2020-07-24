"""
This module was built to generate solution paths for the knight's tour.
Solution paths get outputted to the console. Switch settings on your IDE
to make sure the console output is saved to a file.

Note that this can take up to 16 minutes to run.

The file produced will be 59.6 MB.
"""

from CoverChessBoard.src.Backtracker import *
from CoverChessBoard.src.MakeMovementGraph import *
import time


start = time.time()
matrix = make_n_matrix(8)
board = matrix_to_graph(matrix)
add_movement_edges(board, matrix)

# Create solutions for every square on board
n = len(matrix)
for i in range(0, n):
    for j in range(0, n):
        starting_point = [matrix[i][j]]
        back_tracker(board, starting_point)

end = time.time()
time_taken = end - start
print("Finished process. This took {} many seconds to run.".format(time_taken))