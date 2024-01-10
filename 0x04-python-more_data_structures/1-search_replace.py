#!/usr/bin/python3
from timeit import timeit


def search_replace(my_list, search, replace):
    if my_list is None or len(my_list) == 0:
        return my_list
    new_list = [replace if n == search else n for n in my_list]
    return new_list
