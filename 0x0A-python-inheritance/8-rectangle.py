#!/usr/bin/python3

"""
Work on inherance class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
