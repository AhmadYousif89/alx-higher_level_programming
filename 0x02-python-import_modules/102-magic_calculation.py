#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a: int, b: int) -> int:
    if a < b:
        c: int = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
