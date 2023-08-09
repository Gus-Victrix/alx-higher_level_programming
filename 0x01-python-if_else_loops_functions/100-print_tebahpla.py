#!/usr/bin/python3
for c in range(ord("z"), ord("a") - 1, -1):
    if c % 2 == 1:
        c = c - 32
    print(chr(c), end = "")
