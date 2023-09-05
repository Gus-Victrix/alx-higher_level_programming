#!/usr/bin/python3
"""
Create a class of rectangle
"""


class Rectangle:
    """
    Create a new rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Init the rectangle class
        Args:
            self: The self classes
            width (int): The width
            height (int): The height
        Raises:
            Raises about the setter function
        Returns: Anything
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """
        Give the height
        Args:
            self: The self classes
        Return: The value of of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height
        Args:
            self: The self classes
            value (int): The value to fill
        Raises:
            TypeError: If the height is not an int
            ValueError: If the height is less than 0
        Return: Anything
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    @property
    def width(self):
        """
        Give the width
        Args:
            self: The self classes
        Return: The value of of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width
        Args:
            self: The self classes
            value (int): The value to fill
        Raises:
            TypeError: If the width is not an int
            ValueError: If the width is less than 0
        Return: Anything
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """
        Calculate the area of the rectangle
        Args:
            self: The self classes
        Returns: The area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle
        Args:
            self: The self classes
        Returns: The perimeter, 0 if one of the side is equal to 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """
        Return the rectangle
        Args:
            self: The self classes
        Returns: A string of the rectangle
        """
        string = ""
        for i in range(self.height):
            for j in range(self.width):
                string += "#"
            if i != self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """
        Return a string that show how the class was created
        Args:
            self: The self classes
        Returns: A string that contain show how the class was created
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        Delete a class, print a message
        Args:
            self: The self classes
        Returns: Anything
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
