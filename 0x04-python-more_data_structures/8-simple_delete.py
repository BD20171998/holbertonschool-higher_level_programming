#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):

    for i in a_dictionary:
        if key == i:
            del a_dictionary[i]
            return a_dictionary

    return a_dictionary
