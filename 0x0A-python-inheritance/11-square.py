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


class Square(Rectangle):
    """
    Create a square
    """
    def __init__(self, size):
        """
        Init the square with the parent class
        Args:
            size (int): The size of the square
        Raises:
            TypeError: If size is not an int
            ValueError: If size is less than or equal to 0
        Returns: Anything
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square
        Args:
            self (class)
        Returns: The area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string to explain the class
        Args:
            Self (class)
        Returns: The string
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
