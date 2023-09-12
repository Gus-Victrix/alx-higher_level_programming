#!/usr/bin/python3

"""
Create a class of student
"""


class Student:
    """
    Class of student
    """

    def __init__(self, first_name, last_name, age):
        """
        Init the class with value
        Args:
            self (class)
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        Returns: Anything
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Create a json representation of the class
        Args:
            self (class)
        Returns: The new representation
        """
        if type(attrs) is list and all(type(elem) is str for elem in attrs):
            returnDict = {}
            for elem in attrs:
                if hasattr(self, elem):
                    returnDict[elem] = getattr(self, elem)
            return returnDict
        return vars(self)
