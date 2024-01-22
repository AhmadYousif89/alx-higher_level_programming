#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    result = None

    try:
        result = fct(args[0], args[1])
    except Exception as e:
        print(f"Exception: {e}", file=stderr)

    return result
