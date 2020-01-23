#!/usr/bin/python3


def pascal_triangle(n):
    """Function that creates Pascal’s triangle of size n"""
    if n <= 0:
        return []

    mylist = [[1]]

    for i in range(1, n):
        inlist = []
        temp = []
        temp.insert(0, 0)
        temp += mylist[i - 1].copy()
        temp.append(0)

        for j in range(len(temp) - 1):
            num = 0
            num += temp[j]
            num += temp[j + 1]
            inlist.append(num)
        mylist.append(inlist)

    return mylist
