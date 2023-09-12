#!/usr/bin/python3

"""
Check if the object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    Args:
        obj (Object): The instance to check
        a_class (Object): The specified class
    Returns: True of False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
