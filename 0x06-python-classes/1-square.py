#!/usr/bin/python3
"""Class that defines an empty Square"""


class Square:
    """Create a Square"""

    __size = 0
    """Initialize the Square class"""

    def __init__(self, size=0) -> None:
        self.__size = size
