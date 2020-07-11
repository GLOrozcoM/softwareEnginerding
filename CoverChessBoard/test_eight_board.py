import backtrack_design as bd
import dorff as df

# Set up
matrix = df.make_n_matrix(8)
board = df.matrix_to_graph(matrix)
df.add_movement_edges(board, matrix)

# Create solutions for every square on board
n = len(matrix)
for i in range(0, n):
    for j in range(0, n):
        starting_point = [matrix[i][j]]
        bd.backtracker(board, starting_point)

