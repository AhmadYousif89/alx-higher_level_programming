#!/usr/bin/python3
"""Get the peak element from an unsorted list"""


def get_peak_recursivly(int_list, left, right):
    """
    Finds the peak element in the list recursively.

    Args:
        int_list: The list of integers to search.
        peak: The index of the current element being considered as a peak.

    Returns:
        The peak element in the list, or None if the list is empty.
    """
    mid = (left + right) // 2
    peak = int_list[mid]
    prev_n = int_list[mid - 1]
    next_n = int_list[mid + 1] if mid < len(int_list) - 1 else 0
    # check if the middle element is greater than its neighbors
    if (mid == 0 or prev_n <= peak) and (
        mid == len(int_list) - 1 or next_n <= peak
    ):
        return peak

    # If the left neighbor of `mid` is greater than the middle element,
    # find the peak recursively in the left sublist
    if mid - 1 >= 0 and prev_n > peak:
        return get_peak_recursivly(int_list, left, mid - 1)
    # If the right neighbor of `mid` is greater than the middle element,
    # find the peak recursively in the right sublist
    return get_peak_recursivly(int_list, mid + 1, right)


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
