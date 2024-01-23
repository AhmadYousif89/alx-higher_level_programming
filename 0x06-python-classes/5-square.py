#!/usr/bin/python3
"""Class that defines an empty Square"""


class Square:
    """Create a Square"""

    def __init__(self, size=0):
        """Initialize the Square class"""
        """Args: (self, size=0) size type int"""
        self.size = size

    @property
    def size(self):
        """Get/Set the size of the Square"""
        return self.__size

    @size.setter
    def size(self, value=0):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self) -> int:
        """Calculate the area of the Square"""
        return self.__size * self.__size

    def my_print(self):
        """Print a square shape based on the size property"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            for x in range(self.__size):
                print("#", end='')
            print()
