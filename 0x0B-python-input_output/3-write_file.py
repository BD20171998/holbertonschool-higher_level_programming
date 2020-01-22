#!/usr/bin/python3


"""This is an example of the write_file function

>>> write_file = __import__('3-write_file').write_file
>>> nb_characters = write_file("my_first_file.txt", "Holberton School!\n")
>>> print(nb_characters)
18

"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8) and returns the number
    of characters written
    """
    count = 0

    with open(filename, mode='w+', encoding='utf-8') as f:
        for i in text:
            f.write(i)
            count += 1
        f.close()

    return count
