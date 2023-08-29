#!/usr/bin/python3

"""Define a class named Square"""


class Square:
    """Square Classe"""
    def __init__(self, size=0):
        """
        Init a square
        Args:
            size (int): Size of the square
        Raises:
            TypeError: Error if not an int
            ValueError: Error if not positiv
        Returns: None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
