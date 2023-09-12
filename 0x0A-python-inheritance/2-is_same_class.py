#!/usr/bin/python3

"""
Check if an object is exactly an instance of the specifed class
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specifed class
    Args:
        obj (Object): The instance to check
        a_class (Object): The specified class
    Returns: True of False
    """
    return type(obj) is a_class
