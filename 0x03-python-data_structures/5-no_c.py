#!/usr/bin/python3


def no_c(my_string):

        lst = ""

        for i in range(0, len(my_string)):

            if my_string[i] == "c" or my_string[i] == "C":
                continue

            else:
                lst += lst.join(my_string[i])

        return lst
