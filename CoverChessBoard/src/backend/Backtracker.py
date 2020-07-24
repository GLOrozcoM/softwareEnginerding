"""
This module was built to implement a Warnsdorff approach to solving a Knight's tour with backtracking.
"""
import collections


def get_possible_neighbors(graph, source, visited):
    """Find the possible adjacent moves at source and count adjacent moves for source.
    Adjacent moves only given if not in visited. Output is a dictionary.

    :param graph: A graph of a chess board for possible knight moves.
    :param source: A string coordinate in the matrix of the board to check adjacent move number of.
    :param visited: A list with moves already visited.
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


def reject(graph, candidate):
    """ Give T or F depending on whether a candidate can become a solution.
    A reject is T if no subsequent moves are possible, but empty squares still exist.

    :param graph: A graph containing the chess board.
    :param candidate: A list of ordered string coordinates denoting a path on the board.
    :return: Boolean determining whether the candidate should be rejected or not.
    """
    if candidate is None:
        return True

    n = len(candidate)
    latest_move = candidate[n - 1]
    previous_moves = candidate[0:n - 1]

    next_moves = get_possible_neighbors(graph, latest_move, previous_moves)

    # No subsequent moves were found
    if len(next_moves) == 0:
        # We didn't reach all squares on the board
        if len(candidate) != len(graph):
            return True

    return False


def accept(graph, candidate):
    """ Give T or F depending on whether or not a candidate is a complete solution.

    :param graph: Graph containing chess board.
    :param candidate: A list of moves to evaluate as a solution.
    :return: Boolean indicating whether or not candidate is a solution.
    """
    if candidate is None:
        return False

    # If all nodes haven't been reached, then is not a solution
    if len(graph) != len(candidate):
        return False

    # If moves got repeated then this isn't a solution
    if len(set(candidate)) != len(candidate):
        return False

    return True


def get_warnsdorff_moves(candidate, graph, last_move):
    """ Find the next possible moves according to Warnsdorff's rule for the last move
    seen.

    :param candidate: A list of moves to evaluate as a solution.
    :param graph: Graph containing chess board.
    :param last_move: The most recent move carried out.
    :return:
    """
    possible_next_moves = get_possible_neighbors(graph, last_move, candidate)
    minimum_move_number = min(possible_next_moves.values())
    smallest_moves = [k for k, v in possible_next_moves.items() if v == minimum_move_number]
    return smallest_moves


def back_tracker(graph, candidate):
    """ Find a solution to the Knight's tour using Warnsdorff's rule. Output
    a list of moves to the console.

    :param graph: Graph containing chess board.
    :param candidate: List of moves to be evaluated as a solution.
    :return: A single solution to the Knight's tour as a list of moves.
    """

    # See if this candidate is a solution
    if accept(graph, candidate):
        print(candidate)
        return candidate

    # Reject the solution if it isn't one
    if reject(graph, candidate):
        return

    # Must explore further before accepting or rejecting the solution
    n = len(candidate)
    last_move = candidate[n - 1]
    next_moves = get_warnsdorff_moves(candidate, graph, last_move)

    # Construct a new candidate solution
    choice = next_moves.pop()
    new_candidate = [el for el in candidate]
    new_candidate.append(choice)
    while choice is not None:
        # Recursively explore the extended solution
        back_tracker(graph, new_candidate)
        if len(next_moves) != 0:
            choice = next_moves.pop()

            # Remove previous attempt and try with the next choice
            new_candidate.pop()
            new_candidate.append(choice)
        else:
            choice = None
