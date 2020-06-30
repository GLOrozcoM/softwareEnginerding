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

# Generate list of all matrix nodes present
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

matrix = generate_n_matrix(8)
graph = add_matrix_to_graph(matrix)

edges_graph = add_movement_edges(graph, matrix)
#nx.draw_networkx(edges_graph)
#plt.show()

def choose_smallest_neighbor(graph, source, visited):
    """ In moves, choose the node that results in smallest number of moves.

    :param graph:
    :param source:
    :return:
    """
    adjacent_moves = list(graph.neighbors(source))
    subsequent_move_lengths = collections.defaultdict(list)
    for move in adjacent_moves:
        if move not in visited:
            print("Visited:", visited)
            moves = list(graph.neighbors(move))
            print("Possible moves:", moves)
            subsequent_move_lengths[move] = len(moves)
            #print(subsequent_move_lengths)
    print(subsequent_move_lengths)
    smallest_move = min(subsequent_move_lengths, key = subsequent_move_lengths.get)
    return smallest_move



#next_move = choose_smallest_neighbor(edges_graph, "11")
#print(next_move)

def warnsdorff(graph, source):

    # Can't go back to where we started
    visited = set()
    visited.add(source)

    traversal_node = source

    traversed_list = [traversal_node]
    print(len(graph))
    while len(visited) != len(graph):
        next_move = choose_smallest_neighbor(graph, traversal_node, visited)
        visited.add(next_move)
        traversed_list.append(next_move)
        traversal_node = next_move

    print("Went through entire list")
    return traversed_list

path = warnsdorff(graph, "11")
print(path)

#traversal = list(nx.edge_bfs(edges_graph, "11"))
#print(traversal)
#traversal_list_knight = []
#for pair in traversal:
 #   element = pair[1]
  #  traversal_list_knight.append(element)

#print(traversal_list_knight)