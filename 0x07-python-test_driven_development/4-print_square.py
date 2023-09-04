#!/usr/bin/python3

"""
Task 3 for the 0x07 Python test driven development
Print a square of "#" with a given size
Test are avalaible in /tests/:
    python3 -m doctest -v ./tests/4-print_square | tail -2
"""


def print_square(size):
    """
    Print a square of "#" with a given size
    Args:
        size (int): Height of the square
    Raises:
        TypeError: If the size is not an integer
        ValueError: If the size is less than 0
    Returns: Nothing, just print the rectangle
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    print(("#" * size + '\n') * size, end="")
