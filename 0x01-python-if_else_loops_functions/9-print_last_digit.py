#!/usr/bin/python3
def print_last_digit(number: int) -> int:
    last_digit: int = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
