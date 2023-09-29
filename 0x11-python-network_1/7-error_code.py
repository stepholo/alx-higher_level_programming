#!/usr/bin/python3
""" Module that takes in a URL,
    sends a request to the URL and displays the body of th
    response. If the HTTP status code is greater than or equal to 400,
    print: Error code: followed by the value of the HTTP status code
"""

import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    code = r.status_code
    if code >= 400:
        print(f"Error code: {code}")
    else:
        print(r.text)
