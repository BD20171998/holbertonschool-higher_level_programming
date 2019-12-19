#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    new = []
    for row in matrix:
        temp = list(map(lambda x: x*x, row))
        new.append(temp)

    return new
