#!/usr/bin/python3
def magic_calculation(a: int, b: int, c: int) -> int:
    if a < b:
        return c
    if c > b:
        return a + b
    return a * b - c
