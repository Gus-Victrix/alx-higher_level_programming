#!/usr/bin/python3

"""
Task 3 for the 0x07 Python test driven development
Print 2 new line after "." "?" or ":" of a given text
Test are avalaible in /tests/:
    python3 -m doctest -v ./tests/5-text_indentation | tail -2
"""


def text_indentation(text):
    """
    Print 2 new line after "." "?" or ":" of a given text
    Uses a buffer to not make sys call for each letter
    Args:
        text (str): The given text
    Raises:
        TypeError: If the text isn't an str
    Returns: Nothing, just print the indented text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    buf = " "

    for letter in text:
        buf += letter
        if letter in [".", "?", ":"]:
            while buf[0] == " ":
                buf = buf[1:]
            print("{}".format(buf), end="\n\n")
            buf = ""
    if buf != "":
        while buf != "" and buf[0] == " ":
                buf = buf[1:]
        print("{}".format(buf), end="")
