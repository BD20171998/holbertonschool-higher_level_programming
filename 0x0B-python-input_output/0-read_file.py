#!/usr/bin/python3


"""
>>> read_file = __import__('0-read_file').read_file
>>> read_file("my_file.txt")
This is the only line from a file
"""


def read_file(filename=""):
    """
    This function reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, encoding='utf-8', mode='r') as f:
        print(f.read(), end="")
        f.close()
