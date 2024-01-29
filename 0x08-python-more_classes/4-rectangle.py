#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Create a Rectangle class"""

    def __init__(self, width=0, height=0):
        """
        Initialize new Rectangle object.
        Args:
        - width (optional): type int defaults to 0
        - height (optional): type int defaults to 0
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        Return a Rectangle representation in a string shape using the (#)s
        """
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        for _ in range(self.__height):
            result += '#' * self.__width + '\n'
        return result.strip()

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

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

    def area(self):
        """Gets the area size of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Gets the perimeter size of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2


my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))
