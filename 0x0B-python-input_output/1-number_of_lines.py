#!/usr/bin/python3


"""This is an example of the number_of_lines function

>>> number_of_lines = __import__('1-number_of_lines').number_of_lines
>>> filename = "my_file_0.txt"
>>> nb_lines = number_of_lines(filename)
>>> print("{} has {:d} lines".format(filename, nb_lines))

my_file_0.txt has 4 lines
"""


def number_of_lines(filename=""):
    """
    This function returns the number of lines of a text file
    """
    x = 0
    with open(filename, encoding='utf-8', mode='r') as f:
        for line in f:
            x += 1
        f.close()

    return x
