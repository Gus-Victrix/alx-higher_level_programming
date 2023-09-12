#!/usr/bin/python3

"""
Create a class MyInt, that work differents as int
"""


class MyInt(int):
    """
    Hacking the in class
    """
    def __eq__(self, other):
        """
        Compare two int from int class or subclass
        Args:
            self (class): Our class of int
            other (class): An other class of int (The real one)
        Return: True if not equal, false else
        """
        return int(self) != other

    def __ne__(self, other):
        """
        Compare two int from int class or subclass
        Args:
            self (class): Our class of int
            other (class): An other class of int (The real one)
        Return: True if equal, false else
        """
        return int(self) == other
