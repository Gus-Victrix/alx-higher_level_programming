#!/usr/bin/python3

"""
Task 2 for the 0x07 Python test driven development
Divide a given matrix by a given number
Test are avalaible in /tests/:
    python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
"""


def say_my_name(first_name, last_name=""):
    """
    Say the name of a user, by asking it into arg
    Args:
        first_name (str): The first name of the user
        last_name (str): The last name of the user
    Raises:
        TypeError: If the first_name is not an str
        TypeError: If the last_name is not an str
    Returns: Nothing, only printing on the console
    """

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
