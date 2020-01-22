#!/usr/bin/python3


"""This is an example of the from_json_string function
>>> from_json_string = __import__('6-from_json_string').from_json_string
>>> s_my_list = "[1, 2, 3]"
>>> my_list = from_json_string(s_my_list)
>>> print(my_list)
>>> print(type(my_list))
[1, 2, 3]
<class 'str'>
"""
from json import loads


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure) represented by
    a JSON string
    """
    return loads(my_str)
