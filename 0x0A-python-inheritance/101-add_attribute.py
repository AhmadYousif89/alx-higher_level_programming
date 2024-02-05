#!/usr/bin/python3
"""Defines the add_attribute function."""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.
    Args:
    - obj: The object to which the attribute will be added.
    - attr_name (str): The name of the new attribute.
    - attr_value: The value of the new attribute.
    Raises:
    - TypeError: If the object cannot have a new attribute.
    """
    if not hasattr(obj, "__dict__") and not hasattr(obj, "__slots__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
