#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """Creates the BaseGeometry class."""

    def area(self):
        """Calculates the area of the geometry shape."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the given value is an integer greater than 0.
        Args:
        - name (str): The name of the variable being validated.
        - value (int): The value to be validated.
        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
