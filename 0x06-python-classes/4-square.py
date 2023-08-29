#!/usr/bin/python3

"""Define a class named Square"""


class Square:
    """Square Classe"""
    def __init__(self, size=0):
        """
        Init a square
        Args:
            size (int): Size of the square
        Returns: None
        """
        self.size = size

    @property
    def size(self):
        """
        Acces to size
        Returns: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square
        Args:
            value (int): The new value of the size
        Raises:
            TypeError: Error if not an int
            ValueError: Error if not positiv
        Returns: None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcul the area of the square
        Returns: The area of the square
        """
        return self.__size ** 2
