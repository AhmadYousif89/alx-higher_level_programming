#!/usr/bin/python3
def main() -> None:
    argv: list[str] = sys.argv[1:]
    args_len: int = len(argv)
    s = "argument"
    if args_len == 0:
        print("0 {}s.".format(s))
    elif args_len == 1:
        print("1 {}:".format(s))
    else:
        print("{} {}:".format(args_len, s))

        for i in range(args_len):
            print("{0}: {1}".format(i + 1, argv[i]))


if __name__ == "__main__":
    import sys

    main()
