"""

Process the paths found after running Warnsdorff + backtracking algorithm.

Primary goal: confirm that a path solution exists for every square in an 8 by 8 board.

File contains 154888 records so it can take a while to process.

N solution
-> Create list with matrix coordinates (one dimensional vector).
-> Check the first move in each path. If the move is in the matrix,
pop it.
-> Continue until the end of file or when the vector is empty (we saw every coordinate in the matrix).

Simple to understand, but expensive. We end up checking every line up until the 88 line
when we could simply jump over a few solutions.

Log N solution
-> Create list with matrix coordiantes (one dimenstional vector).
-> Conduct a binary search for a path based on each entry in the vector.
-> If a path isn't found, break and output for which coordinate a path didn't exist.
-> If the loop ends without breaking, a path existed for each square.

"""

def convert_str_list(string):
    """ Take a string that is itself a list of string ints and turn it into a list with string ints.

    :param string: A string that is a list of string ints.
    :return: A list of string ints.
    """
    str_modified = string.strip("][").split(", ")
    for i in range(0, len(str_modified)):
        # As is, str_modified is a list of doubly stringed ints.
        # This removes the outer string.
        str_modified[i] = str_modified[i].strip("'")
    return str_modified

def read_path_solutions(file_name):
    """ Read in a file_name (txt) that contains a different solution path
    per line.

    :return: paths_str A list of strings where each string is a solution path.
    """
    # Read in solutions and split based on new lines
    paths = open(file_name, "r")
    paths_str = paths.read().splitlines()
    return paths_str

def generate_squares():
    """ Make a list of matrix coordinates. (Start at 11 go to 88)

    :return: A list of all matrix coordinates on an 8 by 8 chess board.
    """
    squares = []
    for i in range(1, 9):
        for j in range(1, 9):
            coord = str(i) + str(j)
            squares.append(coord)
    return squares

def get_path(path_start, file_name):
    """ Use binary search to find a solution path beginning at path_start.

    :param file_name: The file (txt) containing solutions for the piece tour.
    :param path_start: A string of two ints indicating a position on an 8 by 8 chess board.
    :return: A list with string coordinates for what squares the piece should move on to cover the board.
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

    # Path not found
    print("Path not found")
    return None

def perform_check(file_name):
    """ Check if all squares in the chess board have a solution path.

    :param file_name: File to look for the solutions in.
    :return: None
    """
    squares = generate_squares()

    n = len(squares)
    for i in range(0, n):
        path_start = squares[i]
        print("Checking path for {}.".format(path_start))
        path = get_path(path_start, file_name)
        if path is None:
            print("Path for {} does not exist.".format(path_start))
            return

    print("Reached the end of the check successfully.")