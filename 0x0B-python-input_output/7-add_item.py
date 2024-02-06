#!/usr/bin/python3
"""Defines the add_args_to_file function."""


def add_args_to_file(argv):
    """
    Appends command line arguments to a list stored in a JSON file.

    The function loads a list from a JSON file named "add_item.json",
    then appends the command line arguments to this list.
    The modified list is then stored back into the same JSON file.

    If the file "add_item.json" does not exist or cannot be parsed
    as JSON, an empty list is used as the starting point.

    Parameters:
    - argv (list): A list of command line arguments.

    Returns:
    None

    Example:
        $ ./program_name apple orange banana
        ### ["apple", "orange", "banana"]
    """
    filename = "add_item.json"
    try:
        my_list = parse_json(filename)
    except (FileNotFoundError, Exception):
        my_list = []
    my_list.extend(argv)
    stringfy(my_list, filename)
    print(my_list)


if __name__ == "__main__":
    import sys

    stringfy = __import__("5-save_to_json_file").save_to_json_file
    parse_json = __import__("6-load_from_json_file").load_from_json_file
    add_args_to_file(sys.argv[1:])
