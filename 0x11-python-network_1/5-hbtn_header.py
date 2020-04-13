#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":

    html = requests.get(sys.argv[1])

    print(html.headers['x-request-id'])
