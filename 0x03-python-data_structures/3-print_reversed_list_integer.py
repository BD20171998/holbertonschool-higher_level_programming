#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    if len(my_list) > 0:

        lst = my_list[::-1]
        for i in range(0, len(my_list)):
            print('{:d}'.format(lst[i]))
