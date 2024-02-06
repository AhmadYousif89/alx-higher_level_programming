#!/usr/bin/python3
"""Defines a load_from_json_file function."""
import json


def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    Args:
    - filename (str): The name of the file.

    Returns:
    The object loaded from the JSON file.

    Example:
        loaded_data = load_from_json_file("input.json")
        This will load the content of the "input.json" file
        and return the corresponding object.
    """
    with open(filename) as file:
        content = file.read()
        return json.loads(content)


# filename = "tests/my_list.json"
# my_list = load_from_json_file(filename)
# print(my_list)
# print(type(my_list))

# filename = "tests/my_dict.json"
# my_dict = load_from_json_file(filename)
# print(my_dict)
# print(type(my_dict))

# try:
#     filename = "my_set_doesnt_exist.json"
#     my_set = load_from_json_file(filename)
#     print(my_set)
#     print(type(my_set))
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     filename = "tests/my_fake.json"
#     my_fake = load_from_json_file(filename)
#     print(my_fake)
#     print(type(my_fake))
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
