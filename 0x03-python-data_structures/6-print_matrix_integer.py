#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for i, n in enumerate(arr):
            print("{:d}".format(n), end=" " if i != len(arr) - 1 else "")
        print()
