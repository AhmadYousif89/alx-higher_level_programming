#!/usr/bin/python3 -B
from add_0 import add


def main() -> None:
    a = 1
    b = 2
    print("{0} + {1} = {2}".format(a, b, add(a, b)))


if __name__ == "__main__":
    main()