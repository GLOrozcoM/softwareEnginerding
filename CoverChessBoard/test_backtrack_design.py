import backtrack_design as bd
import dorff as df

matrix = df.make_n_matrix(8)
board = df.matrix_to_graph(matrix)
df.add_movement_edges(board, matrix)


# Candidate is clearly not to be rejected
c1 = ["11"]
c2 = ["11", "32"]
c3 = ["11", "23"]

# Path that failed
c4 = ['13', '21', '42', '54', '35', '14', '22', '41', '53', '45', '24', '12', '31', '52', '44', '25', '33']
c4 = ['13', '25', '44', '52', '31', '12', '24', '45', '53', '41', '22', '14', '35', '54', '42', '21', '33']

# Path that is long but didn't fail
c5 = ['11', '23', '15', '34', '55', '43', '51', '32', '13', '21', '42', '54', '35', '14', '22', '41', '53', '45', '24', '12', '31', '52', '44', '25']

# Result
print("Rejection suite")
print(bd.reject(board, c1))
print(bd.reject(board, c2))
print(bd.reject(board, c2))
print(bd.reject(board, c4))
print(bd.reject(board, c5))

####

# Clearly not the solution
c1 = ["11"]
c2 = ["11", "32"]

# Path is long but didn't fail
c3 = ['11', '23', '15', '34', '55', '43', '51', '32', '13', '21', '42', '54', '35', '14', '22', '41', '53', '45', '24', '12', '31', '52', '44', '25']

# Path that is a solution
c4 = ['11', '23', '15', '34', '55', '43', '51', '32', '13', '21', '42', '54', '35', '14', '22', '41', '53', '45', '24', '12', '31', '52', '44', '25', "33"]

# Result
print("Acceptance suite")
print(bd.accept(board, c1))
print(bd.accept(board, c2))
print(bd.accept(board, c2))
print(bd.accept(board, c4))

#####
last_move = "32"
print("get_children_candidate() suite")
print(bd.get_children_candidate(c1, board, last_move))

#####


### Possible starting places that should have a solution
c1 = ["11"]
c2 = ["13"]
c3 = ["55"]
c4 = ["44"]

print("Backtracker suite")
# Find a solution from square '11'
solution_c1 = bd.backtracker(board, c1)
solution_c2 = bd.backtracker(board, c2)
solution_c3 = bd.backtracker(board, c3)
solution_c4 = bd.backtracker(board, c4)

print("Solution for 11")
print(solution_c1)

print("Solution for 13")
print(solution_c2)

print("Solution for 55")
print(solution_c3)
