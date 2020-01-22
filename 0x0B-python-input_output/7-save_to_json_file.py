#!/usr/bin/python3


"""This is an example of the save_to_json_file function
>>> save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
>>> filename = "my_list.json"
>>> my_list = [1, 2, 3]
>>> save_to_json_file(my_list, filename)
>>> filename = "my_dict.json"

cat my_list.json ; echo ""
[1, 2, 3]
"""

from json import dump


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file, using a JSON representation
    """
    with open(filename, mode='w+', encoding='utf-8') as f:
        dump(my_obj, f)
        f.close()
