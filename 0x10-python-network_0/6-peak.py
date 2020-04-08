#!/usr/bin/python3


def find_peak(list_of_integers):
    if list_of_integers == [] or list_of_integers is None:
        return None

    temp = list_of_integers[:]
    temp.sort(reverse=True)
    return temp[0]
