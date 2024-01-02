#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{}".format(chr(i + 65) if i % 2 == 0 else chr(i + 97)), end="")
