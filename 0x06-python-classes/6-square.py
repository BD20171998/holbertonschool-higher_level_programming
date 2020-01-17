#!/usr/bin/python3


class Square:
    """empty class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns size as private """

        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')

        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        """Returns position as private """
        return self.__position

    @position.setter
    def position(self, value):
        if (
                len(value) != 2 or type(value) is not tuple or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or value[1] < 0
          ):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """Returns area of square"""

        return self.__size * self.__size

    def my_print(self):
        """Prints a square using the # character, prints blank line if size
        is 0. Prints p[1] new lines if p[1] is greater than 0. Prints p[0]
        spaces before each # character
        """

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()

        if self.__size == 0:
            print()

        else:
            for i in range(self.__size):
                if self.__position[0] > 0:
                    for k in range(self.__position[0]):
                        print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
