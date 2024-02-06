#!/usr/bin/python3
"""Defines a read_file function."""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it.

    Args:
    - filename (str): The file to be read from.
    """
    with open(filename, mode='r', encoding='UTF-8') as f:
        for line in f:
            print(line, end='')


# read_file("tests/my_file_0.txt")
