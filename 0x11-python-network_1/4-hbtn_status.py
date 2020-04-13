#!/usr/bin/python3

import requests

if __name__ == "__main__":

    html = requests.get('https://intranet.hbtn.io/status')

    print("Body response:")
    print("{}{}".format("\t- type: ", type(html.text)))
    print("{}{}".format("\t- content: ", html.text))
