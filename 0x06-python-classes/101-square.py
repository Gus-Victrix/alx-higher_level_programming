#!/usr/bin/python3

"""Define a class named Square"""


class Square:
    """Square Classe"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Init a square
        Args:
            size (int): Size of the square
            position (tuple): Position where the square start
        Returns: None
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """
        Acces to position
        Returns: The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square
        Args:
            value (int): The new value of the position
        Raises:
            TypeError: Error if value not an int tuple
        Returns: None
        """
        if isinstance(value, tuple) and len(value) == 2 \
           and type(value[0]) is int and type(value[1]) is int \
           and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integer")

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

    def my_print(self):
        """
        Print the square
        Returns: Nothing
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """
        Print the square
        Returns: Nothing
        """
        string = ""
        if self.__size == 0:
            pass
        else:
            for i in range(self.position[1]):
                string += '\n'
            for i in range(self.__size):
                for k in range(self.position[0]):
                    string += ' '
                for j in range(self.__size):
                    string += '#'
                if i != self.size - 1:
                    string += '\n'
        return string
