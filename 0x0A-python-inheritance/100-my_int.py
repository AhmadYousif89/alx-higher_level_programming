#!/usr/bin/python3
"""Defines the MyInt class."""


class MyInt(int):
    """
    Creates the MyInt class.
    A rebel that inverts == and != operators.
    """

    def __eq__(self, other):
        """Overrides the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the != operator."""
        return super().__eq__(other)


my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
