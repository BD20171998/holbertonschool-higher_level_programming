#!/usr/bin/python3


class Square:
    """empty class that defines a square"""

    def __init__(self, size=0):
        self.__size = size

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

    def area(self):
        """Returns area of square
            Yields:
                int: area
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints a square using the # character, prints blank line if size
        is 0
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
