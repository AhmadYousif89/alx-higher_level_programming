#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Create a Rectangle class"""

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle class.
        Args:
        - width (optional): type int defaults to 0
        - height (optional): type int defaults to 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/Set the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
