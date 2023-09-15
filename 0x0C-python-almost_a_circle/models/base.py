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
        return

    @staticmethod
    def to_json_string(list_dictionaries):
        import json
        '''
        Creates JSON string representation of the input.

        Args:
            list_dictionaries (list of dictionaries): The input dictionaries.

        Returns:
            JSON representation of list_dictionaries.
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
