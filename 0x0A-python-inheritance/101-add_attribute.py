#!/usr/bin/python3

"""
Add attrbiute to a class is possible
"""


def add_attribute(obj, attribute, value):
    """
    Add attrbiute to a class is possible
    Args:
        obj (class): The class to add an attribute
        attribute (str): Attribute to add
        value (str, int, float...): Value to fill
    Raises:
        TypeError: If we can't add attribute in the class
    Returns: Anything
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
