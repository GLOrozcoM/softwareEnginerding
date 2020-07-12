"""
Develop a Warnsdorff implementation for the Knight's tour.
"""

import networkx as nx
import collections
import matplotlib.pyplot as plt

def knight_moves(i, j, matrix):
    """ The matrix i,j position where the knight is present.

    :param i: Integer starting at 1
    :param j: Integer starting at 1
    :return: List containing places in the matrix the knight can move to.
    """""
    assert i >= 1 and j >= 1, print("i and j must both be greater or equal to 1")
    possible_moves = []
    n = len(matrix)
    # A knight moves in an "L" shape
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            if (col == j - 1) or (col == j + 1):
                if (row == i + 2) or (row == i - 2):
                    possible_moves.append(matrix[row - 1][col - 1])
            elif (row == i + 1) or (row == i - 1):
                if (col == j - 2) or (col == j + 2):
                    possible_moves.append(matrix[row - 1][col - 1])
    return possible_moves

def make_n_matrix(n):
    """ Make an n x n matrix as a list of lists.

    :param n: Dimension of matrix
    :return: A list of lists containing string matrix coordinates.
    """
    matrix = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(str(i) + str(j))
        matrix.append(row)
    return matrix

def matrix_to_graph(matrix):
    """ Get a graph from a matrix.

    :param matrix: A list of lists with string coordinates for a mtrix.
    :return: A networkx Graph with each matrix entry as a node.
    """
    graph = nx.Graph()
    for col in matrix:
        graph.add_nodes_from(col)
    return graph

def make_list_edge_tuples(node, edge_nodes):
    """ Make a list of tuples encoding edges between node and edge nodes.

    :param node: Node to make neighbors of. Assuming a string coordinate in a matrix.
    :param edge_nodes: Edge nodes to be created for the node. Assuming a list of string coordinates in a matrix.
    :return: A list of tuples. Each tuple of the form (node, edge_node).
    """
    tuple_list = []
    for element in edge_nodes:
        edge_tuple = (node, element)
        tuple_list.append(edge_tuple)
    return tuple_list

def add_movement_edges(graph, matrix):
    """ Connect nodes in a graph according to whether a Knight can move across them.

    :param graph: A graph with nodes present.
    :param matrix: A list of lists with matrix string coordinates.
    :return: A graph with edges made according to Knight movement possibility.
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
    """Find the possible adjacent moves at source and count adjacent moves for source.
    Adjacent moves only given if not in visited. Output is a dictionary.

    :param graph: A graph of a chess board for possible knight moves.
    :param source: A string coordinate in the matrix of the board to check adjacent move number of.
    :param visited: A set with moves already visited.
    :return: A dictionary with move keys and the number of further moves possible as values.
    """
    adjacent_moves = list(graph.neighbors(source))
    subsequent_move_lengths = collections.defaultdict(list)
    for move in adjacent_moves:
        if move not in visited:
            next_level_moves = list(graph.neighbors(move))

            # The source is considered visited so we shouldn't include it in our count
            src_index = next_level_moves.index(source)
            next_level_moves.pop(src_index)

            subsequent_move_lengths[move] = len(next_level_moves)

    return subsequent_move_lengths

def choose_next_move_warnsdorff(graph, source, visited):
    """ Get the Warnsdorff rule for the next move in a Knight's tour.

    :param graph: Graph containing possible knight moves connected to each other.
    :param source: Where the knight is on the board.
    :param visited: A set containing visited squares.
    :return: A matrix string coordinate of the chess board.
    """

    # A dictionary of string moves with associated length for each numbers, matrix
    next_possible_moves = get_possible_neighbors(graph, source, visited)

    # Find the minimum value for moves
    minimum_move_number = min(next_possible_moves.values())

    # These moves have the first level smallest moves
    smallest_moves = [k for k, v in next_possible_moves.items() if v == minimum_move_number]
    # No tie happened, a single minimum reached
    if len(smallest_moves) == 1:
        print("A single minimum found.")
        return smallest_moves[0]


    print("Multiple minima found")
    # A tie occured. Iterate over each move and find smallest possible
    # Final move returned isn't coming from the original list at times...
    next_level_moves = collections.defaultdict(list)
    for move in smallest_moves:
        next_neighbors = get_possible_neighbors(graph, move, visited)

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
        print(traversed_list)
        next_move = choose_next_move_warnsdorff(graph, traversal_node, visited)
        visited.add(next_move)
        traversed_list.append(next_move)
        traversal_node = next_move

    print("Visited every node on the graph")
    return traversed_list

