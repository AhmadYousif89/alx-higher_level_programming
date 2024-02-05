#!/usr/bin/python3
"""Defines the lookup function."""


def lookup(obj):
    """
    Gets a list of available attributes and methods of an object.
    Args:
    - obj : The object in test.
    Return:
    - The list of available attributes and methods of an object.
    """
    return dir(obj)
