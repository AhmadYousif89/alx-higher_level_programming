#!/usr/bin/python3
"""Defines a MyList class."""


class MyList(list):
    """Creates the MyList class."""

    def print_sorted(self):
        """Print elements in sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)
