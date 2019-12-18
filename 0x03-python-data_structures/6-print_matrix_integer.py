#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if matrix:
        for i in range(0, len(matrix)):
            x = len(matrix[i])

            for j in range(0, x):
                if j == x - 1 and i != x:
                    print('{:d}'.format(matrix[i][j]))
                    break
                if j == x - 1 and i == x - 1:
                    print('{:d}'.format(matrix[i][j]), end="\n")
                print('{:d} '.format(matrix[i][j]), end="")

    elif matrix == '':
        print('')
