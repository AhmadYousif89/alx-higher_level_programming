#!/usr/bin/python3
def main() -> None:
    argv: list[str] = sys.argv[1:]
    args_len: int = len(argv)

    if args_len == 0:
        print("0 arguments.")
    if args_len > 0:
        print(args_len, "argument{0}:".format("s" if args_len > 1 else ""))

    for i in range(args_len):
        print("{0}: {1}".format(i + 1, argv[i]))


if __name__ == "__main__":
    import sys

    main()
