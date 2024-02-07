#!/usr/bin/python3
"""Define the Log parser functions."""


def log_stats():
    """
    Prints statistics based on the provided file size and status code dict.
    """
    print("File size: {}".format(size))
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    import sys
    from collections import defaultdict

    size = 0
    count = 0
    status_codes = defaultdict(int)

    try:
        for line in sys.stdin:
            line_segments = line.split()
            if len(line_segments) > 1:
                size += int(line_segments[-1])
                code = line_segments[-2]
                status_codes[code] += 1
            count += 1
            if count % 10 == 0:
                log_stats()
        log_stats()
    except KeyboardInterrupt:
        log_stats()
