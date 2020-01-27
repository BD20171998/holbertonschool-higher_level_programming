#!/usr/bin/python3


"""importing json module"""
from json import dumps, dump, loads


class Base:
    """
    Base class that manages the id attribute in all
    future classes and to avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that returns the JSON string representation of
        a list of dictionaries
        """

        if list_dictionaries is None:
            return "[]"

        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes the JSON string representation of a list of
        instances who inherit of class Base to a file
        """
        rs_json = []

        classname = cls.__name__

        if list_objs is not None:

            for i in list_objs:
                rs_json.append(cls.to_dictionary(i))

        else:
            rs_json = '[]'

        with open(classname+".json", mode='w', encoding='utf-8') as f:
            jsonstring = cls.to_json_string(rs_json)
            f.write(jsonstring)

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that returns the list of the JSON string
        representation
        """

        if json_string is None:
            return []

        return loads(json_string)
