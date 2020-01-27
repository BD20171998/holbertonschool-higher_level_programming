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

        jlist = []
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return dumps(jlist)

        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes the JSON string representation of a list of
        instances who inherit of class Base to a file
        """
        rs_json = []
        rs_json2 = []

        if list_objs is None:
            with open("empty.json", mode='a', encoding='utf-8') as g:
                dump(rs_json, g)

        classname = cls.__name__

        for i in list_objs:

            if classname == "Square":

                obj_dict = {}

                xname = "_Rectangle__x"
                xval = i.__dict__[xname]
                obj_dict.update([("x", xval)])

                yname = "_Rectangle__y"
                yval = i.__dict__[yname]
                obj_dict.update([("y", yval)])

                hname = "_Rectangle__height"
                hval = i.__dict__[hname]
                obj_dict.update([("height", hval)])

                wname = "_Rectangle__width"
                wval = i.__dict__[wname]
                obj_dict.update([("width", wval)])

                ival = i.__dict__["id"]
                obj_dict.update([("id", ival)])

                rs_json.append(obj_dict)

            if classname == "Rectangle":

                obj_dict2 = {}

                xname = "_Rectangle__x"
                xval = i.__dict__[xname]
                obj_dict2.update([("x", xval)])

                yname = "_Rectangle__y"
                yval = i.__dict__[yname]
                obj_dict2.update([("y", yval)])

                hname = "_Rectangle__height"
                hval = i.__dict__[hname]
                obj_dict2.update([("height", hval)])

                wname = "_Rectangle__width"
                wval = i.__dict__[wname]
                obj_dict2.update([("width", wval)])

                ival = i.__dict__["id"]
                obj_dict2.update([("id", ival)])

                rs_json2.append(obj_dict2)

        if classname == "Rectangle":
            with open(classname+".json", mode='w', encoding='utf-8') as f:
                dump(rs_json2, f)

        if classname == "Square":
            with open(classname+".json", mode='w', encoding='utf-8') as f:
                dump(rs_json, f)

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that returns the list of the JSON string
        representation
        """

        if json_string is None:
            return []

        return loads(json_string)
