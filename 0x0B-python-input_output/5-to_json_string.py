#!/usr/bin/python3


"""This is an example of the to_json_string function
>>> to_json_string = __import__('5-to_json_string').to_json_string
>>> my_list = [1, 2, 3]
>>> s_my_list = to_json_string(my_list)
>>> print(s_my_list)
>>> print(type(s_my_list))
[1, 2, 3]
<class 'str'>
"""
from json import dumps


def to_json_string(my_obj):
    """Function that returns the JSON representation of an object (string)"""
    return dumps(my_obj)
