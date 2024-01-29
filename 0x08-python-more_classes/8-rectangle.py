#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """
    Create a Rectangle class.
    Attributes:
    - number_of_instances type(int): The number of Rectangle instances.
    - print_symbol type(any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize new Rectangle object.
        Args:
        - width (optional): type int defaults to 0
        - height (optional): type int defaults to 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Return a Rectangle representation in a string shape using the (#)s
        """
        if not self.__width or not self.__height:
            return ""
        result = (str(self.print_symbol) * self.__width + '\n') * self.__height
        return result[:-1]

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Get/Set the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the Rectangle width.
        Args:
        - value: The width value.
        Raises:
        - TypeError: If value is not of type int.
        - ValueError: If value is negative.
        """
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
        """
        Sets the Rectangle height.
        Args:
        - value: The height value.
        Raises:
        - TypeError: If value is not of type int.
        - ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Gets the area size of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Gets the perimeter size of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Gets the Rectangle with the greater area.
        Args:
        - rect_1: The first Rectangle.
        - rect_2: The second Rectangle.
        Raises:
        - TypeError: If either rect_1 or rect_2 is not of type Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
