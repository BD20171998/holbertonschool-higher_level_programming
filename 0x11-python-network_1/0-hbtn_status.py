#!/usr/bin/python3

from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("{:<4s}{}{}".format(" ", "- type: ", type(html)))
        print("{:<4s}{}{}".format(" ", "- content: ", html))
        print("{:<4s}{}{}". format(" ", "- utf8 content: ",
                                   html.decode('utf-8')))
