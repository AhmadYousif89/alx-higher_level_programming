#!/usr/bin/python3
"""Define the Log parser functions."""


def log_stats():
    """
    Prints statistics based on the provided file size and status code dict.
    """
    print(f"File size: {size}")
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print(f"{key}: {value}")


if __name__ == "__main__":
    import sys

    size = 0
    count = 0
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
                size += int(line_segments[-1])
                code = line_segments[-2]
                if code in status_codes:
                    status_codes[code] += 1

            count += 1
            if count % 10 == 0:
                log_stats()
        log_stats()
    except KeyboardInterrupt:
        log_stats()
