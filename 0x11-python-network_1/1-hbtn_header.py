#!/usr/bin/python3
"""Module to define a method to display the
    value of the X-Request-Id variable found
    in the header of the response
"""


import urllib.request as req
from sys import argv


if __name__ == "__main__":
    with req.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
