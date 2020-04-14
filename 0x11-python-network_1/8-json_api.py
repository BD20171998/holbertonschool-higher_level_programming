#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":

    if (len(sys.argv) < 2):
        q = ""

    else:
        q = sys.argv[1]

    try:
        url = 'http://0.0.0.0:5000/search_user'
        html = requests.post(url, data={'q': q})

        response = html.json()

        if response != {}:
            print("[{}] {}".format(response['id'], response['name']))

        elif (response == {}):
            print("No result")

    except ValueError:
        print("Not a valid JSON")
