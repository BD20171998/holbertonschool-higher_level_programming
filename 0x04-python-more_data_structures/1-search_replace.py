#!/usr/bin/python3


def search_replace(my_list, search, replace):

    if my_list:
        newlist = my_list[:]

        for i in newlist:
            if i == search:
                newlist[i] = replace

        return newlist
