#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    if my_list:

        if idx < 0 or idx >= len(my_list):
            return my_list

        elif idx >= 0 and idx < len(my_list):
            lst = my_list[:]
            lst[idx] = element
            return lst
