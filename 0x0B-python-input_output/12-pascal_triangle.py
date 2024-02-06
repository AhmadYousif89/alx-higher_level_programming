#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's Triangle with 'n' rows.

    Args:
    - n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
    A list of lists representing Pascal's Triangle.

    Example:
        triangle = pascal_triangle(5)
        Returns a list representing the first 5 rows of Pascal's Triangle.
    """
    tri = []
    ncr = 0
    for i in range(n):
        row = []
        for j in range(i + 1):
            ncr = _factorial(i) // (_factorial(j) * (_factorial(i - j)))
            row.append(ncr)
        tri.append(row)
    return tri


def _factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
    - n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    The factorial of the input integer.

    Example:
        fact_5 = _factorial(5)
        ### fact_5 -> 120
    """
    if n == 0:
        return 1
    return _factorial(n - 1) * n


# TEST:
# def print_triangle(triangle):
#     """
#     Print the triangle
#     """
#     print(triangle)
#     for row in triangle:
#         print("[{}]".format(",".join([str(x) for x in row])))


# if __name__ == "__main__":
#     tri = pascal_triangle(10)
#     print_triangle(tri)
