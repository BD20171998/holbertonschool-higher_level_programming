#!/usr/bin/python3


def search_replace(my_list, search, replace):

    if not my_list:
        return

    newlist = my_list[:]

    for i in newlist:
        if i == search:
            newlist[i] = replace

    return newlist
