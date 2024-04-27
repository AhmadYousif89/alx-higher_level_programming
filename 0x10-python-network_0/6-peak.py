#!/usr/bin/python3
"""Get the peak element from an unsorted list"""


def get_peak_recursivly(int_list, start, end):
    """
    Finds the peak element in the list recursively.

    Args:
        int_list: The list of integers to search.
        start: The starting index of the list.
        end: The ending index of the list.

    Returns:
        The peak element in the list.
    """
    mid = (start + end) // 2
    peak = int_list[mid]
    prev_n = int_list[mid - 1]
    next_n = int_list[mid + 1] if mid < len(int_list) - 1 else 0

    # check if the peak element is greater than its neighbors
    if prev_n <= peak and peak >= next_n:
        return peak
    # Search left if peak is less than the left neighbor
    if peak < prev_n:
        return get_peak_recursivly(int_list, start, mid - 1)
    # Search right if peak is greater than the right neighbor
    return get_peak_recursivly(int_list, mid + 1, end)


def find_peak(list_of_integers):
    """
    Finds the peak element in the list.

    Args:
        list_of_integers: The list of integers to search.

    Returns:
        The peak element in the list, or None if the list is empty.
    """
    if list_of_integers is None or not list_of_integers:
        return None

    return get_peak_recursivly(list_of_integers, 0, len(list_of_integers))


if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2]))
    print(find_peak([]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
