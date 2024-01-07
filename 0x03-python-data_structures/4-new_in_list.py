#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    count = len(my_list)
    if idx < 0 or idx >= count:
        return my_list
    new_list = []
    for i in range(count):
        new_list.insert(i, my_list[i])
        if i == idx:
            new_list.remove(my_list[i])
            new_list.insert(i, element)
    return new_list
