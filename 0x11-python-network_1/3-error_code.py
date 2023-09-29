#!/usr/bin/python3
"""Module takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8).
"""


from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as req:
            content = req.read().decode('utf8')
            print(content)
    except HTTPError as e:
        print(f"Error code: {e.code}")
