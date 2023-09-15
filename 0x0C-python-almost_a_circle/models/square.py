#!/usr/bin/python3
'''This module defines the class square'''
from models.rectangle import Rectangle

class Square(Rectangle):
    '''This is a template for square objects.'''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initializes square instances.

        Args:
            size (int): The dimensions of the square.
            x (int): The x co-ordinate of the square.
            y (int): The y co-ordinate of the square.
            id (int): The identification of the object instance.
        '''
        super().__init__(size, size, x, y, id)
        self.size = size
        return

    def __str__(self):
        '''
        The informal string representation of the object.

        Returns:
            String representation of the object.
        '''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width)

    @property
    def size(self):
        '''
        Accessor of the size attribute of the square instance.

        Returns:
            The current size of the object.
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        Mutator of the size attribute of the square object.

        Args:
            value (int): The new value to be assigned as object size.
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        return
