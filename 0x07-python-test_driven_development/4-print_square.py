#!/usr/bin/python3
"""Defines a square-printing function"""


def print_square(size):
    """
    Print a square shape using the (#) sympol.
    Args:
    - size (int): The height/width of the square.
    Raises:
    - TypeError: size is not an integer
    - ValueError: size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")


# print_square(4)
# print("")
# print_square(6)
# print("")
# print_square()
# print("")
# print_square(1)
# print("")
# try:
#     print_square(-1)
# except Exception as e:
#     print(e)
# print("")
