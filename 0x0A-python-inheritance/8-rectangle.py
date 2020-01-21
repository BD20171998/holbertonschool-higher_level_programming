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
