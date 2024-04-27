#!/usr/bin/env python3
"""Get the peak element from an unsorted list"""


def find_peak(A):
    """find pick element"""
    if A == []:
        return None

    def recursive(A, left=0, right=len(A) - 1):
        """helper recursive function"""

        mid = (left + right) // 2

        # check if the middle element is greater than its neighbors
        if (mid == 0 or A[mid - 1] <= A[mid]) and (
            mid == len(A) - 1 or A[mid + 1] <= A[mid]
        ):
            return A[mid]

        # If the left neighbor of `mid` is greater than the middle element,
        # find the peak recursively in the left sublist
        if mid - 1 >= 0 and A[mid - 1] > A[mid]:
            return recursive(A, left, mid - 1)

        # If the right neighbor of `mid` is greater than the middle element,
        # find the peak recursively in the right sublist
        return recursive(A, mid + 1, right)

    return recursive(A)


if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2]))
    print(find_peak([]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
