"""
Develop moves for queen to cover entire board
"""

def forward_row_step(j):
    column = []
    for i in range(1, 9):
        column.append(str(i) + str(j))
    return column

def backward_row_step(j):
    column = []
    for i in range(8, 0, -1):
        column.append(str(i) + str(j))
    return column

full_move_list = []
for j in range(1, 9):
    if (j % 2) == 0:
        backward = backward_row_step(j)
        full_move_list += backward
    else:
        forward = forward_row_step(j)
        full_move_list += forward

print(full_move_list)
