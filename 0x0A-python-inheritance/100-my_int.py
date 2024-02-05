#!/usr/bin/python3
"""Defines the MyInt class."""


class MyInt(int):
    """
    Creates the MyInt class.
    A rebel that inverts == and != operators.
    """

    def __eq__(self, value):
        """Overrides the == operator."""
        return super().__ne__(value)

    def __ne__(self, value):
        """Overrides the != operator."""
        return super().__eq__(value)
