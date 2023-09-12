#!/usr/bin/python3

"""
Work on inherance class
"""

Rectangle = __import__('9-rectangle').Rectangle


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
