#!/usr/bin/python3
def safe_print_integer(value):
    is_int = isinstance(value, int)
    try:
        if is_int:
            print("{0}".format(value))
            return True
    except:
        return False
