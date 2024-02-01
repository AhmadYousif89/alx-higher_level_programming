#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.
    Args:
    - matrix (list): A list of lists of ints or floats.
    - div (int/float): The divisor.
    Raises:
    - TypeError: If matrix is not a list
                 the matrix length is zero
                 the sub-lists are not of type list or of different sizes.
    - TypeError: If the matrix contains a non-number elements.
    - TypeError: If divisor is not an int or float.
    - ZeroDivisionError: If divisor is zero.
    Returns:
    - A new matrix after division
    """
    # check if the matrix or its sub-lists are of type list
    if (
        matrix is None
        or len(matrix) == 0
        or not isinstance(matrix, list)
        or any(not isinstance(arr, list) for arr in matrix)
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # check the type of each element in the sub-list
    for arr in matrix:
        if any(not isinstance(elem, (int, float)) for elem in arr):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    # check the type and value of the divider
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # check that all sub-lists have the same size
    if any(len(arr) != len(matrix[0]) for arr in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(el / div, 2) for el in arr] for arr in matrix]
    return new_matrix
