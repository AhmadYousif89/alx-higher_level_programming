#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(list, map(lambda row: map(lambda x: x**2, row), matrix)))
