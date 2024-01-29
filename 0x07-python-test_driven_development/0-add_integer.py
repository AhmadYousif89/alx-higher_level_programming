#!/usr/bin/python3
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """
    Addition of two numbers.
    Parameters:
    - a: number of typr int or float.
    - b: number of typr int or float.
    Raises:
    - TypeError: If a or b is a non-integer and non-float.
    """
    if not type(a) == int and not type(a) == float:
        raise TypeError("a must be an integer")
    if not type(b) == int and not type(b) == float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/0-add_integer.txt")


# print(add_integer(1, 2))
# print(add_integer(100, -2))
# print(add_integer(2))
# print(add_integer(100.3, -2))
# try:
#     print(add_integer(4, "School"))
# except Exception as e:
#     print(e)
# try:
#     print(add_integer(None))
# except Exception as e:
#     print(e)
