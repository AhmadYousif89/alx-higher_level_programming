#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return
    for key, value in sorted(a_dictionary.items()):
        print("{0}: {1}".format(key, value))
