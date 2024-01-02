#!/usr/bin/python3
def remove_char_at(str: str, n: int) -> str:
    for i in str:
        if n > len(str) or n < 0:
            return str
        elif i == str[n]:
            return str.replace(str[n], "")

    return str
