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
        if type(width) is not int:
            raise TypeError('width must be an integer')

        if width <= 0:
            raise ValueError('width must be > 0')

        self.__width = width

    @property
    def height(self):
        """Returns height as private """
        return self.__height

    @height.setter
    def height(self, height):
        """Sets height value as private from user"""
        if type(height) is not int:
            raise TypeError('height must be an integer')

        if height <= 0:
            raise ValueError('height must be > 0')

        self.__height = height

    @property
    def x(self):
        """Returns x as private """
        return self.__x

    @x.setter
    def x(self, x):
        """Sets x value as private from user"""
        if type(x) is not int:
            raise TypeError('x must be an integer')

        if x < 0:
            raise ValueError('x must be >= 0')

        self.__x = x

    @property
    def y(self):
        """Returns y as private """
        return self.__y

    @y.setter
    def y(self, y):
        """Sets y value as private from user"""
        if type(y) is not int:
            raise TypeError('y must be an integer')

        if y < 0:
            raise ValueError('y must be >= 0')

        self.__y = y
