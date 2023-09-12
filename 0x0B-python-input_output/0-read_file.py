#!/usr/bin/python3

"""
Read a file
"""


def read_file(filename=""):
    """
    Read a file
    """
    with open(filename, "r", encoding="utf-8") as fl:
        print(fl.read(), end="")
