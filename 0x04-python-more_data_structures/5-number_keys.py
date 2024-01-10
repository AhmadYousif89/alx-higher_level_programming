#!/usr/bin/python3
def number_keys(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return 0
    return len(a_dictionary.keys())
