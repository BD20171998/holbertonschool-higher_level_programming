#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":

    url = 'https://api.github.com/user'

    html = requests.get(url, auth=(sys.argv[1], sys.argv[2]))

    my_dict = html.json()

    print(my_dict.get('id'))
