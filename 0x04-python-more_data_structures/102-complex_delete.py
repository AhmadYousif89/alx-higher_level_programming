#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None or not isinstance(a_dictionary, dict):
        return {}

    keys_to_delete = [k for k, v in a_dictionary.items() if v == value]
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary
