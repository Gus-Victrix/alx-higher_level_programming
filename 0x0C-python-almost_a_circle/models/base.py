#!/usr/bin/python3
'''This module defines the Base class of this project.'''
import json


class Base:
    '''The base class of this project, tracks objects via id.'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Initializes all objects of this project.

        Args:
            id (int): This is the id to be assigned to the new object.
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        return

    @staticmethod
    def to_json_string(list_dictionaries):
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

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Writes the JSON string representation of list_objs to a file.

        Args:
            List_objs (list of objects): The list to be saved into a file.
        '''
        filename = cls.__name__ + ".json"
        list_dictionaries = []
        if list_objs is not None:
            for obj in list_objs:
                list_dictionaries.append(cls.to_dictionary(obj))
        with open(filename, "w+", encoding='utf-8') as f:
            f.write(cls.to_json_string(list_dictionaries))
        return

    @staticmethod
    def from_json_string(json_string):
        '''
        Converts a json string into a dictionary list.

        Args:
            json_string (string): String representation of a dictionary list.

        Returs:
            List formed from the JSON string.
        '''
        if json_string is not None and json_string != "":
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        '''
        Args:
            dictionary (dict): The dictionary containing the attributes of
                                the instance.

        Returns:
            An instance with all attributes alredy set.
        '''
        if len(dictionary):
            if cls.__name__ == "Square":
                dummy = cls(1)
            else:
                dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''
        Loads instance data from a json file.

        Returns:
            List of instances if present. Else, an empty list is returned.
        '''
        filename = cls.__name__ + ".json"
        temp = []

        with open(filename, "r+", encoding="utf-8") as f:
            for a in cls.from_json_string(f.read()):
                temp.append(cls.create(**a))
        except FileExistsError:
            return []
        return temp

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save instances into cvs file
        Args:
            list_objs (list): List of obj to save into csv
        Returns: Anything
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w+", encoding="utf-8") as f:
            writer = csv.writer(f)
            for elem in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                        [elem.id, elem.width, elem.height, elem.x, elem.y]
                        )
                else:
                    writer.writerow([elem.id, elem.size, elem.x, elem.y])
        return

    @classmethod
    def load_from_file_csv(cls):
        """
        Load instance from csv file
        Args:
        Returns: A list of all instances
        """
        filename = cls.__name__ + ".csv"
        listOfObjs = []
        try:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                for elem in reader:
                    if cls.__name__ == "Rectangle":
                        newObj = {
                            "id": int(elem[0]),
                            "width": int(elem[1]),
                            "height": int(elem[2]),
                            "x": int(elem[3]),
                            "y": int(elem[4]),
                        }
                    else:
                        newObj = {
                            "id": int(elem[0]),
                            "size": int(elem[1]),
                            "x": int(elem[2]),
                            "y": int(elem[3]),
                        }
                    newObj = cls.create(**newObj)
                    listOfObjs.append(newObj)
            return listOfObjs
        except FileExistsError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw the given rectangle, or square
        Args:
            list_rectangles (list): List of all instances of rectangle to draw
            list_squares (list): list of all instances of square to draw
        """
        wn = turtle.Screen()
        turtle.bgcolor("#61657F")
        myLittleTurtle = turtle.Turtle()
        myLittleTurtle.shape("circle")

        for elem in list_rectangles:
            myLittleTurtle.up()
            myLittleTurtle.goto(elem.x, elem.y)
            myLittleTurtle.down()
            for i in range(2):
                myLittleTurtle.fd(elem.width)
                myLittleTurtle.lt(90)
                myLittleTurtle.fd(elem.height)
                myLittleTurtle.lt(90)

        for elem in list_squares:
            myLittleTurtle.up()
            myLittleTurtle.goto(elem.x, elem.y)
            myLittleTurtle.down()
            for i in range(4):
                myLittleTurtle.fd(elem.size)
                myLittleTurtle.lt(90)

        myLittleTurtle.hideturtle()
        turtle.exitonclick()
        return
