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

    def __eq__(self, other: 'Square'):
        """Override the equality operator."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other: 'Square'):
        """Override the inequality operator."""
        if isinstance(other, Square):
            return self.area() != other.area()
        return True

    def __gt__(self, other: 'Square'):
        """Override the greater than operator."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other: 'Square'):
        """Override the greater than or equal operator."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other: 'Square'):
        """Override the less than operator."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other: 'Square'):
        """Override the less than or equal operator."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
