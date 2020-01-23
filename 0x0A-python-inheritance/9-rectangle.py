#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Class Rectangle"""


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """Instantiation of inputs"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Function that returns area"""
        return self.__height * self.__width

    def __str__(self):
        """Returns rectangle description"""
        return '[{}] {}/{}'.format(self.__class__.__name__, self.__width,
                                   self.__height)
