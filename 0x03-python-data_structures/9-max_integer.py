#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    max_int = my_list[0]
    for i in my_list:
        if max_int < i:
            max_int = i
    return max_int


my_list = None
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
