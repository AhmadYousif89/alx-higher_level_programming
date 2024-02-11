#!/usr/bin/python3
"""Defines a Rectangle class."""
from .base import Base


class Rectangle(Base):
    """Represents a Rectangle object."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
        -   width (int): Width of the rectangle.
        -   height (int): Height of the rectangle.
        -   x (int): x-coordinate of the rectangle (default is 0).
        -   y (int): y-coordinate of the rectangle (default is 0).
        -   id (int): Optional identifier for the rectangle.

        Rasies:
        -   TypeError -
            If the value of width, height, x, or y is not an integer.
        -   ValueError -
            If width or height <= 0 or if x or y < 0
        """
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Return a string representation of the Rectangle object."""
        return "[Rectangle] ({id}) {x}/{y} - {w}/{h}".format(
            id=self.id, x=self.x, y=self.y, w=self.width, h=self.height
        )

    @property
    def width(self):
        """Set/Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/Get the x offset of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/Get the y offset of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """
        Update a Rectangle instance.

        Args:
        *args (ints): New attribute values.
            -   1st argument represent id attribute.
            -   2nd argument represent width attribute.
            -   3rd argument represent height attribute.
            -   4th argument represent x attribute.
            -   5th argument represent y attribute.

        **kwargs (dict): A key/value pairs of new set of attributes.
        """
        prefix = "_Rectangle__"
        attrs = [key.replace(prefix, '') for key in self.__dict__.keys()]
        # 👆 more dynamic than 👉 attrs = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, value in enumerate(args):
                if i < len(attrs):  # handle index out of range
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle object."""
        prefix = "_Rectangle__"
        attrs = [key.replace(prefix, '') for key in self.__dict__.keys()]
        new_dict = {key: getattr(self, key) for key in attrs}
        return new_dict
