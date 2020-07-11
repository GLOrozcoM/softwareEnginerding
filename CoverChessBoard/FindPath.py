"""

Develop a way to query for the desired solution path for the knight's tour.

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

def get_path(path_start):
    """ Use binary search to find the path in solution space.

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