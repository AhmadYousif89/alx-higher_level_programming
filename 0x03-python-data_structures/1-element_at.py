#!/usr/bin/python3
from typing import Union


def element_at(my_list: list[int], idx: int) -> Union[int, None]:
    count: int = len(my_list)
    if idx < 0 or idx >= count:
        return None
    for i in range(count):
        if i == idx:
            return my_list[i]
