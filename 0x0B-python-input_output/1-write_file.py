#!/usr/bin/python3
"""Defines a write_file function."""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8).

    Args:
    - filename (str): The file to be read from.

    Return:
    The number of created bytes.
    """
    with open(filename, mode='w', encoding='UTF-8') as f:
        nb = f.write(text)
    return nb


# nb_characters = write_file(
#     "./tests/my_first_file.txt", "This School is so cool!\n"
# )
# print(nb_characters)
