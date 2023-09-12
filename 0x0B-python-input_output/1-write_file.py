#!/usr/bin/python3

"""
Write into a file
"""


def write_file(filename="", text=""):
    """
    Write into a file
    """
    with open(filename, "w+", encoding="utf-8") as fl:
        return fl.write(text)
