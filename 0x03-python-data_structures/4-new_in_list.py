#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    if idx < 0 or idx >= len(my_list):
        return my_list

    elif idx > 0 and idx < len(my_list):
        lis = []
        lis[len(lis):] = [element]
        lst = my_list[0:idx] + lis + my_list[idx+1:]
        return lst

    else:
        lis = []
        lis[len(lis):] = [element]
        return lst
