#!/usr/bin/python3


"""
This is an example of the print_square function.
>>> print_square(2)
##
##
"""


def print_square(size):
    """This function prints a square using a '#' """
    if isinstance(size, float) is True and size < 0:
        raise TypeError('size must be an integer')

    if isinstance(size, int) is True and size < 0:
        raise ValueError('size must be >= 0')

    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size == 0:
        print()

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
