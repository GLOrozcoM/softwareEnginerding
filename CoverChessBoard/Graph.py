"""
Develop a way to use the graph
"""

import networkx as nx
import collections
import matplotlib.pyplot as plt


# Knight move calculator
def knight_moves(i, j, matrix):
    """ The matrix i,j position where the knight is present

    :param i:
    :param j:
    :return: List containing places in the matrix the knight can move to.
    """""

    # A knight moves in an "L" shape
    possible_moves = []

    n = len(matrix)
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            if (col == j - 1) or (col == j + 1):
                if (row == i + 2) or (row == i - 2):
                    possible_moves.append(matrix[row - 1][col - 1])
            elif (row == i + 1) or (row == i - 1):
                if (col == j - 2) or (col == j + 2):
                    possible_moves.append(matrix[row - 1][col - 1])
    return possible_moves

def generate_n_matrix(n):
    matrix = []
    for i in range(1, n + 1):
        col = []
        for j in range(1, n + 1):
            col.append(str(i) + str(j))
        matrix.append(col)
    return matrix

# Add to nodes
def add_matrix_to_graph(matrix):
    graph = nx.Graph()
    for col in matrix:
        graph.add_nodes_from(col)
    return graph

def make_list_edge_tuples(node_name, list_nodes):
    """ Make an edge between node and everything in list_nodes

    :param node:
    :param list_nodes:
    :return:
    """
    tuple_list = []
    for element in list_nodes:
        edge_tuple = (node_name, element)
        tuple_list.append(edge_tuple)
    return tuple_list

def add_movement_edges(graph, matrix):
    """

    :param graph: Assume nodes were already added
    :param matrix:
    :return:
    """
    n = len(matrix)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            moves = knight_moves(i, j, matrix)
            current_node = str(i) + str(j)
            edges = make_list_edge_tuples(current_node, moves)
            graph.add_edges_from(edges)
    return graph

def get_possible_neighbors(graph, source, visited):
    """ In moves, choose the node that results in smallest number of moves.

    :param graph:
    :param source:
    :return:
    """
    adjacent_moves = list(graph.neighbors(source))
    subsequent_move_lengths = collections.defaultdict(list)
    for move in adjacent_moves:
        if move not in visited:
            moves = list(graph.neighbors(move))
            subsequent_move_lengths[move] = len(moves)
    return subsequent_move_lengths

def choose_next_move_warnsdorff(graph, source, visited):

    # A dictionary of string moves with associated length for each numbers, matrix
    next_possible_moves = get_possible_neighbors(graph, source, visited)

    # Find the minimum value for moves
    minimum_move_number = min(next_possible_moves.values())

    # These moves have the first level smallest moves
    smallest_moves = [k for k, v in next_possible_moves.items() if v == minimum_move_number]
    print(smallest_moves)

    # No tie happened, a single minima reached
    if len(smallest_moves) == 1:
        print("No tie")
        return smallest_moves[0]


    # A tie occured. Iterate over each move and find smallest possible
    # Final move returned isn't coming from the original list at times...
    next_level_moves = collections.defaultdict(list)
    for move in smallest_moves:
        visited.add(move)
        next_neighbors = get_possible_neighbors(graph, move, visited)
        visited.remove(move)

        #print("Next neighbors", next_neighbors)

        minimum_next = min(next_neighbors.values())

        next_level_moves[move] = minimum_next

    final_move = min(next_level_moves, key = next_level_moves.get)

    return final_move

def warnsdorff(graph, source):

    # Can't go back to where we started
    visited = set()
    visited.add(source)

    traversal_node = source

    traversed_list = [traversal_node]
    while len(visited) != len(graph):
        next_move = choose_next_move_warnsdorff(graph, traversal_node, visited)
        visited.add(next_move)
        traversed_list.append(next_move)
        traversal_node = next_move

    print("Visited every node on the graph")
    return traversed_list

##### Testing ######

matrix = generate_n_matrix(5)
graph = add_matrix_to_graph(matrix)
add_movement_edges(graph, matrix)

path = warnsdorff(graph, "44")

#### No square is visited twice
path_unique = set(path)
print(len(path_unique) == len(path))
#####

#### Visited all nodes in graph
nodes = graph.number_of_nodes()
print(len(path_unique) == nodes)


print(path)
