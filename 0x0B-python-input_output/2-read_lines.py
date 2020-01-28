#!/usr/bin/python3


"""This is an example of the read_lines function

>>> read_lines = __import__('2-read_lines').read_lines
>>> print("1 line:")
>>> read_lines("my_file_0.txt", 1)
Holberton School offers a truly innovative approach to education:

"""


def read_lines(filename="", nb_lines=0):
    """
    This function reads n lines of a text file (UTF8) and prints
    it to stdout. Reads entire file for nb_lines <= 0
    """
    with open(filename, encoding='utf-8', mode='r') as f:
        x = 0

        if nb_lines <= 0 or nb_lines is None:
            print(f.read(), end='')
            f.close()
            return

        else:
            for line in f:
                if x == nb_lines - 1:
                    print(line, end='')
                    f.close()
                    return

                print(line, end='')
                x += 1
        f.close()
