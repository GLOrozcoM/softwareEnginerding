"""
This module was built to encapsulate finding a list of moves covering the chess board from a file name.
"""


def convert_str_list(string):
    """ Take a string that is itself a list of string ints and turn it into a list with string ints.

    :param string: A string that is a list of string ints. Example: '['1', '2']'.
    :return: A list of string ints. Example: ['1', '2'].
    """
    str_modified = string.strip("][").split(", ")
    for i in range(0, len(str_modified)):
        # As is, str_modified is a list of doubly stringed ints.
        # This removes the outer string.
        str_modified[i] = str_modified[i].strip("'")
    return str_modified


def read_path_solutions(file_name):
    """ Read in a .txt file that contains a different solution path
    per line.

    :return: paths_str A list of strings where each string is a solution path.
    """
    paths = open(file_name, "r")
    paths_str = paths.read().splitlines()
    return paths_str


def get_path(path_start, file_name):
    """ Use binary search to find a solution path beginning at path_start.

    :param file_name: The file containing solutions for the piece tour.
    :param path_start: A string of two ints indicating a position on an 8 by 8 chess board. Example: '11'.
    :return: A list with string coordinates for what squares the piece should move to to cover the board.
    """

    paths_str = read_path_solutions(file_name)

    n = len(paths_str)
    left = 0
    right = n - 1
    while left < right:
        middle = round((left + right) / 2 + 0.5)
        converted_path = convert_str_list(paths_str[middle])
        if converted_path[0] == path_start:
            return converted_path
        if converted_path[0] > path_start:
            right = middle - 1
        else:
            left = middle - 1

    converted_path = convert_str_list(paths_str[left])
    if converted_path[0] == path_start:
        return converted_path

    print("Path not found")
    return None