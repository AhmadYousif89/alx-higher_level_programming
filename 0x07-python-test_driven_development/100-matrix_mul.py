#!/usr/bin/python3
"""Defines a matrix_mul function"""


def matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices.
    Args:
    - m_a (list of lists): The first matrix.
    - m_b (list of lists): The second matrix.
    Raises:
    - TypeError: If the input matrices do not meet the specified requirements.
    - ValueError: If the matrices cannot be multiplied.
    Returns:
    - list of lists: The resulting matrix after multiplication.
    """
    # Validate m_a:
    if not isinstance((m_a), list):
        raise TypeError("m_a must be a list")
    if any(not isinstance(arr, list) for arr in m_a):
        raise TypeError("m_a must be a list of lists")
    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    for arr in m_a:
        if any(not isinstance(el, (int, float)) for el in arr):
            raise TypeError("m_a should contain only integers or floats")
    if any(len(arr) != len(m_a[0]) for arr in m_a[1:]):
        raise TypeError("each row of m_a must be of the same size")

    # Validate m_b:
    if not isinstance((m_b), list):
        raise TypeError("m_b must be a list")
    if any(not isinstance(arr, list) for arr in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    for arr in m_b:
        if any(not isinstance(el, (int, float)) for el in arr):
            raise TypeError("m_b should contain only integers or floats")
    if any(len(arr) != len(m_b[0]) for arr in m_b[1:]):
        raise TypeError("each row of m_b must be of the same size")

    # check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # extract the matrices sizes
    rows_ma, cols_ma = len(m_a), len(m_a[0])
    cols_mb = len(m_b[0])
    # initialize the new_matrix with zero values
    new_matrix = [[0 for _ in range(cols_mb)] for _ in range(rows_ma)]

    for row in range(rows_ma):
        for cell in range(cols_mb):
            for idx in range(cols_ma):
                new_matrix[row][cell] += m_a[row][idx] * m_b[idx][cell]

    return new_matrix
