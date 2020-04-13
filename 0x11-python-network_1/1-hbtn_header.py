#!/usr/bin/python3

from sys import argv
from urllib.request import urlopen, urlretrieve

if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        allinfo = response.info()

        headers = allinfo.__dict__['_headers']

        header_dict = {k: v for k, v in headers}

        print(header_dict['X-Request-Id'])
