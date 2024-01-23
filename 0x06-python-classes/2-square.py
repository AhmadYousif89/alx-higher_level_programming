#!/usr/bin/python3
"""Class that defines an empty Square"""


class Square:
    """Create a Square"""

    __size = 0
    """Initialize the Square class"""
    """Args: (self, size=0) size type int"""

    def __init__(self, size=0) -> None:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
