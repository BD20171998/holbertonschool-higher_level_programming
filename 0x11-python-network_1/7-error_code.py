#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":

    try:
        html = requests.get(sys.argv[1])
        html.raise_for_status()

    except requests.exceptions.HTTPError:
        print("Error code: {}".format(html.status_code))

    else:
        print(html.text)
