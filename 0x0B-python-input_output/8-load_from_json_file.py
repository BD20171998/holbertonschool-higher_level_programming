#!/usr/bin/python3


"""This is an example of the load_from_json_file function
>>> load_from_json_file = __import__('load_from_json_file').load_from_json_file
>>> filename = "my_list.json"
>>> my_list = load_from_json_file(filename)
>>> print(my_list)
>>> print(type(my_list))
[1, 2, 3]
<class 'list'>

"""

from json import load


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        x = load(f)
        f.close()
    return x
