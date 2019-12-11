#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):

        letter = str[i]
        ascvalue = ord(letter)

        if ascvalue >= 97 and ascvalue <= 122:
            ascvalue = ascvalue - 32

        print('{}'.format(chr(ascvalue)), end="")

    print('')
