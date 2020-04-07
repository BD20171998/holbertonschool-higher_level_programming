#!/usr/bin/python3


def find_peak(list_of_integers):
    if list_of_integers == [] or list_of_integers is None:
        return None
    else:
        return(max(list_of_integers))
