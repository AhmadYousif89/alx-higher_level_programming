#!/usr/bin/python3
"""Defines a save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a JSON file.

    Parameters:
    - my_obj (any): The object to be saved as JSON file.
    - filename (str): The name of the file.

    Example:
        save_to_json_file({"key": "value"}, "output.json")
        This will save the dictionary {"key": "value"} to a file named "output.json".
    """
    with open(filename, mode='w') as file:
        file.write(json.dumps(my_obj))


# filename = "my_list.json"
# my_list = [1, 2, 3]
# save_to_json_file(my_list, filename)

# filename = "my_dict.json"
# my_dict = {
#     'id': 12,
#     'name': "John",
#     'places': ["San Francisco", "Tokyo"],
#     'is_active': True,
#     'info': {'age': 36, 'average': 3.14},
# }
# save_to_json_file(my_dict, filename)

# try:
#     filename = "my_set.json"
#     my_set = {132, 3}
#     save_to_json_file(my_set, filename)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
