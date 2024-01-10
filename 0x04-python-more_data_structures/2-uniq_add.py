#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    unique_list = set(my_list)
    return sum(n for n in unique_list)
