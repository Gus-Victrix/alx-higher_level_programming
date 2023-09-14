#!/usr/bin/python3

class Base:
    '''The base class of this project, tracks objects via id.'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Initializes all objects of this project.

        Args:
            id (int): This is the id to be assigned to the new object.
        '''
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
