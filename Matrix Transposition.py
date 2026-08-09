#Matrix Transposition
# Write a function that takes a 2D matrix (list of lists) and returns its transpose (rows become columns).env

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix)) for i in range(len(matrix[0]))]]
