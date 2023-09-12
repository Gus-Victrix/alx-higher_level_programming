#!/usr/bin/python3

"""
Check is the obj is an instance of the class, or from inherited class
"""


def is_kind_of_class(obj, a_class):
    """
    Check is the obj is an instance of the class, or from inherited class
    Args:
        obj (Object): The instance to check
        a_class (Object): The specified class
    Returns: True of False
    """
    return isinstance(obj, a_class)
