#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    This class creates new instances only for attributes called "first_name".
    """

    __slots__ = ["first_name"]
