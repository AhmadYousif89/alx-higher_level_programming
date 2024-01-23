#!/usr/bin/python3
"""Class that defines an empty Square"""


class Square:
    """Create a Square"""

    def __init__(self, size=0, position: tuple[int, int] = (0, 0)):
        """Initialize the Square class.

        Args:
            size (int): The size of the square.
            position (tuple[int, int]): The position of the square.
        """
        self.size = size
        self.position = position

    def area(self) -> int:
        """Calculate the area of the Square"""
        return self.__size * self.__size

    @property
    def size(self) -> int:
        """Get/Set the size of the Square"""
        return self.__size

    @size.setter
    def size(self, value=0) -> None:
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size: int = value

    @property
    def position(self) -> tuple[int, int]:
        """Get/Set the position of the Square."""
        return self.__position

    @position.setter
    def position(self, position: tuple[int, int] = (0, 0)) -> None:
        if (
            not isinstance(position, tuple)
            or position[0] < 0
            or position[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position: tuple[int, int] = position

    def my_print(self) -> None:
        """Print a square shape based on the size property"""
        if self.__size == 0:
            print()
            return
        if self.__position[1]:
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
