#!/usr/bin/python3
"""Defines the append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a text after each line containing a searched string in a file.

    Args:
    - filename (str): The name of the file to be modified.
    - search_string (str): The string to search for in each line.
    - new_string (str): The string to be inserted.

    Returns:
    None
    """
    if not filename or not search_string or not new_string:
        return

    with open(filename, mode='r') as rf:
        lines = rf.readlines()
    with open(filename, mode='w') as wf:
        for line in lines:
            wf.write(line)
            if search_string in line:
                wf.write(new_string)


# append_after("tests/append_after_100.txt", "Python", "\"C is fun!\"\n")
