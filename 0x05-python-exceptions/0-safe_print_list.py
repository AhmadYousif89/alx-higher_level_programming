#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print("{0}".format(my_list[i]), end="" if i < x - 1 else "\n")
            count += 1
    except IndexError:
        print()

    return count
