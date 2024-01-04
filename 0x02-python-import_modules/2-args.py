#!/usr/bin/python3
def main() -> None:
    count: int = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))


if __name__ == "__main__":
    import sys

    main()
# argv: list[str] = sys.argv[1:]
#     args_len: int = len(argv)
#     if args_len == 0:
#         print("0 arguments.")
#     if args_len > 0:
#         print("{0} argument{1}:".format(args_len, "s" if args_len > 2 else ""))
#         for i in range(args_len):
#             print("{0}: {1}".format(i + 1, argv[i]))
