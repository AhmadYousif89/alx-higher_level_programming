#!/usr/bin/python3
def main() -> None:
    argv: list[str] = sys.argv[1:]
    args_len: int = len(argv)
    total = 0

    if args_len == 0:
        print("0")
    if args_len > 0:
        for i in range(args_len):
            total += int(argv[i])
        print("{0}".format(total))


if __name__ == "__main__":
    import sys

    main()
