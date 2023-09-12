#!/usr/bin/python3

"""
Work on inherance class
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
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """
    Create a rectangle
    """
    def __init__(self, width, height):
        """
        Init the rectangle
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        Raises:
            TypeError: If width or height is not an int
            ValueError: If one of these two is less than of equal to 0
        Returns: Anything
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle
        Args:
            self (class)
        Returns: The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string to explain the class
        Args:
            Self (class)
        Returns: The string
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
