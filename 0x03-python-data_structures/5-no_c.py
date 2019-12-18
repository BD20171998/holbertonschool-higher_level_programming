#!/usr/bin/python3
def no_c(my_string):

    if my_string:
        lst = my_string[:]
        a = ["c", "C"]
        lst = "".join(i for i in lst if i not in a)
        return lst
