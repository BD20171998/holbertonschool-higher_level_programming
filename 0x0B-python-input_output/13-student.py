#!/usr/bin/python3


class Student:

    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method that retrieves a dictionary representation of a Student
        instance
        """
        if attrs is not None:
            Dict = {k: v for k, v in self.__dict__.items() if k in attrs}
            return Dict

        else:
            Dict = self.__dict__
            return Dict

    def reload_from_json(self, json):
        """
        Method that replaces all attributes of the Student instance
        """
        if len(json) == 0:
            pass

        else:
            self.first_name = json['first_name']
            self.last_name = json['last_name']
            self.age = json['age']
