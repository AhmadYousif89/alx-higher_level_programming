#!/usr/bin/python3
"""Defines a Square class."""
from .rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square object."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int): x-coordinate of the square (default is 0).
            y (int): y-coordinate of the square (default is 0).
            id (int): Optional identifier for the square.
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Return a string representation of the Square object."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Set/Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def display(self):
        """Print the Square using the `#` character."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """
        Update a Square instance.

        Args:
        *args (ints): New attribute values.
            -   1st argument represent id attribute.
            -   2nd argument represent size attribute.
            -   3rd argument represent x attribute.
            -   4th argument represent y attribute.

        **kwargs (dict): A key/value pairs of new set of attributes.
        """
        prefix = "_Rectangle__"
        attrs = [
            key.replace(prefix, '')
            .replace('width', 'size')
            .replace('height', 'size')
            for key in self.__dict__.keys()
        ]  # ['id', 'size', 'size', 'x', 'y']
        attrs.remove('size')
        # print(attrs) ['id', 'size', 'x', 'y']
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
        attributes = [
            key.replace(prefix, '')
            .replace('width', 'size')
            .replace('height', 'size')
            for key in self.__dict__.keys()
        ]
        attributes.remove('size')
        new_dict = {key: getattr(self, key) for key in attributes}
        return new_dict
