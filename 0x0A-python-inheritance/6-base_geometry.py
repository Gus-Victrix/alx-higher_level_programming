#!/usr/bin/python3

"""
Create a class for geometry
"""


class BaseGeometry:
    """
    Base of geometry
    """
    def area(self):
        """
        Calculate the area of the geometry model
        """
        raise Exception('area() is not implemented')
