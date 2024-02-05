#!/usr/bin/python3
"""Defines the sub-class Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates a Rectangle class using the base class (BaseGeometry)."""

    def __init__(self, width, height):
        """
        Intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Return a string representation of a the Rectangle class."""
        return f"Rectangle {self.__width}/{self.__height}"

    def area(self):
        """Returns the area of the Rectangle."""
        return self.__width * self.__height
