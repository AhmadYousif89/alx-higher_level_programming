#!/usr/bin/python3
"""Class that defines an empty Square"""


class Square:
    """Create a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square class.

        Args:
            size (int): The size of the square.
            position (tuple[int, int]): The position of the square.
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculate the area of the Square"""
        return self.__size * self.__size

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

    @property
    def position(self):
        """Get/Set the position of the Square."""
        return self.__position

    @position.setter
    def position(self, value=(0, 0)):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
            or any(i < 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Print a square shape based on the size property"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
