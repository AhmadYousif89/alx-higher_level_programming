#!/usr/bin/python3
"""Define the Log parser functions."""
import sys


def log_stats(size, status_codes):
    """
    Prints statistics based on the provided file size and status code dict.

    Args:
    - size (int): Total file size.
    - status_codes (dict): A dict containing counts for different status codes.

    Prints:
    - File size: Total file size.
    - Number of lines for each status code.
    - Only prints statistics for status codes that have appeared in the input.
    """
    print(f"File Size: {size}")
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print(f"{key}: {value}")


counter = 0
total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}


try:
    for line in sys.stdin:
        line_segments = line.split()
        if len(line_segments) > 1:
            total_size += int(line_segments[-1])
            code = line_segments[-2]
            if code in status_codes:
                status_codes[code] += 1
        counter += 1
        if counter % 10 == 0:
            log_stats(total_size, status_codes)
    log_stats(total_size, status_codes)
except KeyboardInterrupt:
    log_stats(total_size, status_codes)
