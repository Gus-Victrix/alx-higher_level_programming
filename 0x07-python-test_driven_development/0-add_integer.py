#!/usr/bin/python3

"""
Task 0 for the 0x07 Python test driven development
Add two integers
Test are avalaible in /tests/:
    python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
"""


def add_integer(a, b=98):
    """
    Add two integer, in case of float, cast it into int
    Args:
        a (int, float): First num to add
        b (int, float): Second num to add
    Raises:
        TypeError: If given arg is not an int, or not castable into int
    Returns: Return the sum of the two int, or error if any issues
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError('a must be an integer')
    if not isinstance(b, int):
        raise TypeError('b must be an integer')

    return a + b
