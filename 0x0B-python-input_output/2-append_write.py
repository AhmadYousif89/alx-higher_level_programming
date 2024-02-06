#!/usr/bin/python3
"""Defines a write_file function."""


def append_write(filename="", text=""):
    """
    Appends a string to a text file.

    Args:
    - filename (str): The file to be read from.
    - text (str): The content to write.

    Return:
    The number of created bytes.
    """
    with open(filename, mode='a', encoding='UTF-8') as f:
        nb = f.write(text)
    return nb


# nb_characters_added = append_write(
#     "tests/file_append.txt", "This School is so cool!\n"
# )
# print(nb_characters_added)
