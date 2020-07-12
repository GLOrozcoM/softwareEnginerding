"""

Use this modul to check that all viable pieces have a solution path for every
square on the chess board.

"""

from CoverChessBoard.CheckPathsComplete import *

print("Knight's tour check")
knight_tour = "SolutionPaths/knight_tour.txt"
perform_check(knight_tour)
print("Knight's tour check ended")