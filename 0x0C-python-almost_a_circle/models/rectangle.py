#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    '''Template for Rectangle objects.'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Constructor of Rectangle objects.

        Args:
            width (int): The width to be assigned to the rectangle.
            height (int): The height to be assigned to the rectangle.
            x (int): The x-co-ordinate of the origin of the rectangle.
            y (int): The y-co-ordinate of the origin of the rectangle.
            id (id): The id to be assigned to the new object.
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        return

    @property
    def width(self):
        '''
        Accessor of the rectangle width.

        Returns:
            The width attribute of the rectangle.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Mutator of the width attribute of a rectangle object.

        Args:
            value (int): Value to be assigned to the width of the rectangle.
        '''
        attr = "width"
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr))
        if value <= 0:
            raise ValueError("{} must be > 0".format(attr))
        self.__width = value
        return

    @property
    def height(self):
        '''
        Accessor of the height attribute of the rectangle object.

        Returns:
            The height of the rectangle object.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Mutator of the height attribute of a rectangle object.

        Args:
            value (int): To become the new height attribute of the rectangle.
        '''
        attr = "height"
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr))
        if value <= 0:
            raise ValueError("{} must be > 0".format(attr))
        self.__height = value
        return

    @property
    def x(self):
        '''
        Accessor of the x-co-ordinate attribute of a rectangle.

        Returns:
            The x co-ordinate of the rectangle object.
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Mutator of the x co-ordinate of rectangle instance.

        Args:
            value (int): The new value for the x attribute of rectangle.
        '''
        attr = "x"
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr))
        if value < 0:
            raise ValueError("{} must be >= 0".format(attr))
        self.__x = value
        return

    @property
    def y(self):

        '''
        Accessor of the y attribute of the rectangle instance.

        Returns:
            The value of y attribute of the rectangle.
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Mutator of the y attribute.

        Args:
            value (int): The new value of y attribute.
        '''
        attr = "y"
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr))
        if value < 0:
            raise ValueError("{} must be >= 0".format(attr))
        self.__y = value
        return

    def area(self):
        '''
        Calculates the area of the rectangle isinstance.

        Returns:
            Area of rectangle.
        '''
        return self.__width * self.__height

    def display(self):
        ''' Prints the rectangle instance using specified symbol (#)default.'''
        for i in range(self.__height):
            print("{}".format("#" * self.__width))
        return
