#!/usr/bin/python3
import sys


def main(argv: list[str]) -> None:
    args_len: int = len(argv)
    if args_len == 0:
        print("0 arguments.")
    if args_len > 0:
        print("{0} argument{1}:".format(args_len, "s" if args_len > 2 else ""))
        for i, arg in enumerate(argv, 1):
            print("{0}: {1}".format(i, arg))


if __name__ == "__main__":
    main(sys.argv[1:])
