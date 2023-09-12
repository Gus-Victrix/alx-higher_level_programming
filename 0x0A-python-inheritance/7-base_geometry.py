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

    def integer_validator(self, name, value):
        """
        Check if an given arg is correct
        Args:
            self (class)
            name (str): The name of the var
            value (int): The value to fill
        Raises:
            TypeError: If the value is not an int
            ValueError: If the calue is less than of equal to 0
        Returns: Anything
        """
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
