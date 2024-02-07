#!/usr/bin/python3
"""Define the Log parser functions."""


def log_stats():
    """
    Prints statistics based on the provided file size and status code dict.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    count = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for line in sys.stdin:
            line = line.split()
            if len(line) > 1:
                size += int(line[-1])
                code = line[-2]
                if code in valid_codes:
                    if status_codes.get(code, -1) == -1:
                        status_codes[code] = 1
                    else:
                        status_codes[code] += 1

            count += 1
            if count % 10 == 0:
                log_stats()
        log_stats()

    except KeyboardInterrupt:
        log_stats()
        raise
