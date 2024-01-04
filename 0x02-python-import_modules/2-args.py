#!/usr/bin/python3
import sys


def main() -> None:
    argv: list[str] = sys.argv[1:]
    args_len: int = len(argv)
    if args_len == 0:
        print("0 arguments.")
    if args_len > 0:
        print("{0} argument{1}:".format(args_len, "s" if args_len > 2 else ""))
        for i in range(args_len):
            print("{0}: {1}".format(i + 1, argv[i]))


if __name__ == "__main__":
    main()
