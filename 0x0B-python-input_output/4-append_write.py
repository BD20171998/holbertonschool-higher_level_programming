#!/usr/bin/python3


"""This is an example of the append_write function
>>> append_write = __import__('4-append_write').append_write
>>> nb_characters_added = append_write("file_append.txt", "Holberton School \
... is so cool!\n")
>>> print(nb_characters_added)
29
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of  a text file (UTF8) and
    returns the number of characters written
    """
    count = 0

    with open(filename, mode='a+', encoding='utf-8') as f:
        for i in text:
            f.write(i)
            count += 1
        f.close()

    return count
