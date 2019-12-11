#!/usr/bin/python3
def remove_char_at(str, n):

    if n > 0 and n < len(str) - 1:
        nstr = str[0:n] + str[n+1:]
        return nstr

    elif n == len(str) - 1:
        nstr = str[0:n-1]
        return nstr

    elif n == 0:
        nstr = str[1:]
        return nstr

    elif n >= len(str) or n < 0:
        return str
