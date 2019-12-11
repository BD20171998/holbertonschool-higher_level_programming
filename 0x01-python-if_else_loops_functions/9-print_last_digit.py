#!/usr/bin/python3
def print_last_digit(number):

    if number < 0:
        mod = (-number) % 10

    elif number > 0:
        mod = number % 10

    elif number == 0:
        mod = 0

    print('{}'.format(mod), end="")

    return mod
