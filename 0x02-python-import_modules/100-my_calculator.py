#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main() -> None:
    argv: list[str] = sys.argv
    args_len: int = len(argv) - 1
    if args_len < 3:
        print("Usage: {0} <a> <operator> <b>".format(argv[0]))
        sys.exit(1)

    argA: int = int(argv[1])
    argB: int = int(argv[3])
    op: str = argv[2]

    if op == "+":
        print("{0} + {1} = {2}".format(argA, argB, add(argA, argB)))
    elif op == "-":
        print("{0} - {1} = {2}".format(argA, argB, sub(argA, argB)))
    elif op == "*":
        print("{0} * {1} = {2}".format(argA, argB, mul(argA, argB)))
    elif op == "/":
        print("{0} / {1} = {2}".format(argA, argB, div(argA, argB)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == "__main__":
    main()
