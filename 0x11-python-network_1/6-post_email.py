#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":

    myobj = {'email': sys.argv[2]}

    try:
        html = requests.post(sys.argv[1], data=myobj)

        print(html.text)

    except:
        pass
