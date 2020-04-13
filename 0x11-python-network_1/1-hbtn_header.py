#!/usr/bin/python3

from sys import argv
from urllib.request import urlopen, Request

if __name__ == "__main__":
    req = Request(argv[1])
    with urlopen(req) as response:

        allinfo = response.info()

        headers = allinfo.__dict__['_headers']

        header_dict = {k: v for k, v in headers}

        print(header_dict['X-Request-Id'])
