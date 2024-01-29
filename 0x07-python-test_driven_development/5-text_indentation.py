#!/usr/bin/python3
"""Defines a text-indentation function"""


def text_indentation(text=""):
    """
    Print a text with 2 newlines after each of these characters: (., ?, :)
    Args:
    - text (type string): The text to print.
    Raises:
    - TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delims = ('.', '?', ':')
    new_text = ""

    for ch in text:
        if ch in delims:
            new_text += ch + '\n\n'
        else:
            new_text += ch

    lines = new_text.split('\n')
    for i, line in enumerate(lines):
        print(line.strip(), end='' if i == len(lines) - 1 else '\n')
