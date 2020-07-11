"""

Process the paths found after running Warnsdorff + backtracking algorithm.

Primary goal: confirm that a path solution exists for every square in an 8 by 8 board.

N solution
-> Check number of lines in file, curiosity.
->> 154888 solutions generated.
-> Create list with matrix coordinates (one dimensional vector).
-> Check the first move in each path. If the move is in the matrix,
pop it.
-> Continue until the end of file or when the vector is empty (we saw every coordinate in the matrix).

Log N solution (amortized?)
-> Use a version of binary search

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

# Read in solutions and split based on new lines
paths = open("PathsOutput/back_out.txt", "r")
paths_str = paths.read().splitlines()

# Vector of all coordinates to be popped as encountered in solutions
squares = []
for i in range(1, 9):
    for j in range(1, 9):
        coord = str(i) + str(j)
        squares.append(coord)

# Start processing file
num_lines = len(paths_str)
print("There are {} solutions in this file.".format(num_lines))

for i in range(0, num_lines):
    converted = convert_str_list(paths_str[i])
    path_start = converted[0]
    if path_start in squares:
        print("{} has a solution".format(path_start))
        squares.remove(path_start)
        print("Current squares:{}".format(squares))

    if len(squares) == 0:
        print("All path starts have a solution path.")
        break

print("Reached end of process")
print("The remainder of squares in squares vector: {}".format(squares))
