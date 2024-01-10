#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None or len(matrix) == 0:
        return matrix

    new_matrix = list(map(lambda arr: [i**2 for i in arr], matrix))
    return new_matrix
