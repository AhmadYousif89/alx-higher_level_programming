#!/usr/bin/python3
def uppercase(str: str) -> None:
    for ch in str:
        print(chr(ord(ch) - 32) if 'a' <= ch <= 'z' else ch, end="")
    print()
