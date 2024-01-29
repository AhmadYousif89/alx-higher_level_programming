#!/usr/bin/python3
"""Defines a lazy_matrix_mul function"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices using the NumPy lib.
    Args:
    - m_a (list of lists): The first matrix.
    - m_b (list of lists): The second matrix.
    Returns:
    -  The resulting matrix after multiplication.
    """
    return np.matmul(m_a, m_b)
