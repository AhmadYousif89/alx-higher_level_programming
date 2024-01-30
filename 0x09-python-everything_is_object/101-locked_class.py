#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    This class creates new instances only for attributes called "first_name".
    """

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(
                f"'LockedClass' object has no attribute '{name}'"
            )
        super().__setattr__(name, value)
