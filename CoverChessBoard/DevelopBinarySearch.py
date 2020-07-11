"""

Make a binary search algorithm for finding paths in solutions file.

"""

def convert_str_list(string):
    """ Take a string that is a list of string ints and turn it into a list with string ints.

    :param string:
    :return:
    """
    str_modified = string.strip("][").split(", ")
    for i in range(0, len(str_modified)):
        str_modified[i] = str_modified[i].strip("'")
    return str_modified

def read_solutions():
    """

    :return: paths_str
    """
    # Read in solutions and split based on new lines
    paths = open("PathsOutput/back_out.txt", "r")
    paths_str = paths.read().splitlines()
    return paths_str

def get_path_n(path_start):
    """ Give a square of the chess board and output a solution path from the solution paths file.

    :param path_start: A string of matrix coordinates.
    :return: A list of matrix string coordinates of a knight's tour solution.
    """

    paths_str = read_solutions()

    # TODO improve runtime by using a binary search
    num_lines = len(paths_str)
    for i in range(0, num_lines):
        converted = convert_str_list(paths_str[i])
        path_start_file = converted[0]
        if path_start == path_start_file:
            return converted
    print("Path start not found in solution.")

    return None

def get_path_logn(path_start):
    """

    :param path_start:
    :return:
    """

    paths_str = read_solutions()

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


# Tests
p1 = "81"
#path_n = get_path_n(p1)
path_logn = get_path_logn(p1)
#print(path_n)
print(path_logn)