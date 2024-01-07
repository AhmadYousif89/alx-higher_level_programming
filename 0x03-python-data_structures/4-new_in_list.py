#!/usr/bin/python3
def new_in_list(my_list: list[int], idx: int, element: int) -> list[int]:
    new_list: list[int] = []
    count: int = len(my_list)
    if idx < 0 or idx >= count:
        return my_list
    for i in range(count):
        new_list.insert(i, my_list[i])
        if i == idx:
            new_list.remove(my_list[i])
            new_list.insert(i, element)
    return new_list


def main() -> None:
    my_list: list[int] = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list: list[int] = new_in_list(my_list, idx, new_element)
    print(new_list)
    print(my_list)


if __name__ == "__main__":
    main()
