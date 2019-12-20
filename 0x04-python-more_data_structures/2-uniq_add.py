#!/usr/bin/python3


def uniq_add(my_list=[]):

    mysum  = 0
    x = list(set(my_list))

    for i in x:
        mysum = i + mysum

    return mysum
