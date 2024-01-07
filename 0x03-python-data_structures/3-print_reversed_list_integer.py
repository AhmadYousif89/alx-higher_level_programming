#!/usr/bin/python3
def print_reversed_list_integer(my_list: list[int] = []) -> None:
    count: int = len(my_list) - 1
    for i in range(count, -1, -1):
        print("{:d}".format(my_list[i]))


def main() -> None:
    my_list: list[int] = [-1, 0, 1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)


if __name__ == "__main__":
    main()
