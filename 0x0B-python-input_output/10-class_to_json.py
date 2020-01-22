#!/usr/bin/python3


"""This is an example of the class_to_json function

>>> MyClass = __import__('10-my_class').MyClass
>>> class_to_json = __import__('10-class_to_json').class_to_json

>>> m = MyClass("John")
>>> m.number = 89
>>> mj = class_to_json(m)

>>> print(type(mj))
<class '10-my_class.MyClass'>
[MyClass] John - 89

>>> print(m)
<class 'dict'>
{'name': 'John', 'number': 89}

"""


def class_to_json(obj):
    """This function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object
    """

    Dict = obj.__dict__

    return Dict
