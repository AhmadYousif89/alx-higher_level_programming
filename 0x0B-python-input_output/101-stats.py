#!/usr/bin/python3
"""Reads from standard input and computes metrics."""
import sys
from collections import defaultdict


def main():
    """
    Reads input lines from sys.stdin, processes each line, and prints
    statistics every 10 lines or after a keyboard interruption.


    Metrics computed:
    - Total file size
    - Number of lines by status code (200, 301, 400, 401, 403, 404, 405, 500)
    """
    counter = 0
    total_size = 0
    status_codes = defaultdict(int)

    try:
        for line in sys.stdin:
            line_segments = line.split()
            total_size += int(line_segments[-1])
            code = line_segments[-2]

            # Using defaultdict behavior to handle initialization automatically
            status_codes[code] += 1

            counter += 1

            if counter % 10 == 0:
                print_statistics(total_size, status_codes)

    except EOFError:
        print_statistics(total_size, status_codes)


def print_statistics(size, status_codes):
    """
    Prints statistics with total file size and status code counts.

    Parameters:
    - size (int): Total file size.
    - status_codes (dict): A Dict containing counts for different status codes.

    Prints:
    - File size: Total file size.
    - Number of lines for each status code.
    - Only prints statistics for status codes that have appeared in the input.
    """
    print(f"File Size: {size}")
    for key in sorted(status_codes.keys()):
        count = status_codes[key]
        if count > 0:
            print(f"{key}: {count}")


if __name__ == "__main__":
    main()
