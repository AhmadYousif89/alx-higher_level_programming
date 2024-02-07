#!/usr/bin/python3
"""Define the Log parser functions."""
import sys


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


def log_stats():
    """
    Prints statistics based on the provided file size and status code dict.

    Prints:
    - File size: Total file size.
    - Number of lines for each status code.
    - Only prints statistics for status codes that have appeared in the input.
    """
    print(f"File Size: {total_size}")
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print(f"{key}: {value}")


try:
    for line in sys.stdin:
        line_segments = line.split()
        if len(line_segments) >= 2:
            total_size += int(line_segments[-1])
            code = line_segments[-2]
            if code in status_codes:
                status_codes[code] += 1
        counter += 1
        if counter % 10 == 0:
            log_stats()
    log_stats()
except KeyboardInterrupt:
    log_stats()
