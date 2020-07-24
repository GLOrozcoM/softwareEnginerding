"""
This module was built to hold the graph of movements for the knight.
"""

import networkx as nx


def knight_moves(i, j, matrix):
    """ The matrix i,j position where the knight is present. Necessary for connecting edges in 
    graph.

    :param i: Integer starting at 1 representing row.
    :param j: Integer starting at 1 representing column.
    :return: List containing places in the matrix the knight can move to.
    """""
    assert i >= 1 and j >= 1, print("i and j must both be greater or equal to 1")
    possible_moves = []
    n = len(matrix)
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            # A knight moves in an "L" shape
            # -- two rows and one column, or two columns and one row
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
    """ Add matrix nodes to a graph.

    :param matrix: A list of lists with string coordinates for a matrix.
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
