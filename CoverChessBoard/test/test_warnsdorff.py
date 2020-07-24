from CoverChessBoard.src.backend.MakeMovementGraph import *

##### Testing ######

matrix = make_n_matrix(5)
board = matrix_to_graph(matrix)
add_movement_edges(board, matrix)

# Set for get_possible_neighbors()
visited = set("11")
adjacent_moves_11 = get_possible_neighbors(board, "11", visited)
print(adjacent_moves_11)


path = warnsdorff(board, "11")

########## Testing ideas ##############

#### No square is visited twiceR
#path_unique = set(path)
#print(len(path_unique) == len(path))
#####

#### Visited all nodes in graph
#nodes = graph.number_of_nodes()
#print(len(path_unique) == nodes)

########## Testing ideas ##############