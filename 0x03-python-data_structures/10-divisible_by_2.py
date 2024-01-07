#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    _list = []
    for n in my_list:
        trueOrFalse = n % 2 == 0
        _list.append(trueOrFalse)
    return _list
