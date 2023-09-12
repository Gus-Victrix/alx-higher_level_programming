#!/usr/bin/python3

"""
Append into a file
"""


def append_write(filename="", text=""):
    """
    Append into a file
    """
    with open(filename, "a+", encoding="utf-8") as fl:
        return fl.write(text)
