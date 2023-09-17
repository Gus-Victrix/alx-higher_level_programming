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
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
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

    def update(self, *args, **kwargs):
        '''
        Simultaneously updates the attributes of the square object.

        Args:
            args (list): The new values of: id, size, x, y in that order.
            kwargs (dictionary): The key = value pairs to be used for updating.
        '''
        if len(args):
            i = 0
            for a in args:
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
                i += 1
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
        return

    def to_dictionary(self):
        '''
        Creates a dictionary representation of the square object.

        Returns:
            Dictionary representation of the square.
        '''
        a = super().to_dictionary()

        a['size'] = self.size
        a.pop('height')
        a.pop('width')

        return a
