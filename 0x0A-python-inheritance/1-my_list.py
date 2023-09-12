#!/usr/bin/python3

"""
Create a child class from the list one
"""


class MyList(list):
    """
    Child class from list one
    """

    def print_sorted(self):
        """
        print the list in the sorted way
        Args:
            self (class): The list
        Returns: Anything
        """
        print(sorted(self))
