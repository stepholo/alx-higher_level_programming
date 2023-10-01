#!/usr/bin/python3
"""Module that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]

    payload = {'q': q}

    try:
        req = requests.post(url, data=payload)
        req_json = req.json()

        if req_json:
            if 'id' in req_json and 'name' in req_json:
                output = f"[{req_json['id']}] {req_json['name']}"
                print(output)
            else:
                print('No result')
        else:
            print('No result')
    except ValueError:
        print('Not a valid json')
