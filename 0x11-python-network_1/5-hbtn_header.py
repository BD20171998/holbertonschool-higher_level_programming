#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":

    html = requests.get(sys.argv[1])

    html_head_dict = html.headers

    print(html_head_dict['x-request-id'])
