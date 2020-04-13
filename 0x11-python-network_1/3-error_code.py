#!/usr/bin/python3

from sys import argv
from urllib.request import Request, urlopen
from urllib.error import URLError

if __name__ == "__main__":
        req = Request(argv[1])

        try:
                with urlopen(req) as response:
                        html = response.read().decode('utf-8')

        except URLError as e:
                if hasattr(e, 'code'):
                        print('Error code:', e.code)

        else:
                print(html)
