#!/usr/bin/python3
def print_list_integer(my_list: list[int] = []) -> None:
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))


def main() -> None:
    my_list: list[int] = [1, 2, 3, 4, 5]
    print_list_integer(my_list)


if __name__ == "__main__":
    main()
