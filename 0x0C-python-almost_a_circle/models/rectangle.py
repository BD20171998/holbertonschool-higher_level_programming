#!/usr/bin/python3


from models.base import Base


class Rectangle(Base):
    """Class that defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        if id is not None:
            self.id = id

        else:
            super().__init__()

    @property
    def width(self):
        """Returns width as private """
        return self.__width

    @width.setter
    def width(self, width):
        """Sets width value as private from user"""
        self.__width = width

    @property
    def height(self):
        """Returns height as private """
        return self.__height

    @height.setter
    def height(self, height):
        """Sets height value as private from user"""
        self.__height = height

    @property
    def x(self):
        """Returns x as private """
        return self.__x

    @x.setter
    def x(self, x):
        """Sets x value as private from user"""
        self.__x = x

    @property
    def y(self):
        """Returns y as private """
        return self.__y

    @y.setter
    def y(self, y):
        """Sets y value as private from user"""
        self.__y = y
