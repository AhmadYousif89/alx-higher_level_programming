#!/usr/bin/python3
"""Defines the sub-class Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a Square class that inherites from the (Rectangle) class."""

    def __init__(self, size):
        """
        Intialize a new Square.
        Args:
            size (int): The size of the new Square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Return a string representation of a the Square class."""
        return f"Square {self.__size}/{self.__size}"

    def area(self):
        """Returns the area of the Square."""
        return self.__size * self.__size
