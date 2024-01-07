#!/usr/bin/python3
def element_at(my_list, idx):
    count: int = len(my_list)
    if idx < 0 or idx >= count:
        return None
    for i in range(count):
        if i == idx:
            return my_list[i]
