#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        print(
            "{}{}".format(i, j), end=", " if not (i == 8 and j == 9) else "\n"
        )
