#!/usr/bin/python3
"""Module that takes URL and an email, sends a POST
    requests to the passed url with the email parameter,
    and displays the body of the response (decoded in utf-8)
"""


import urllib.request as req
import urllib.parse as par
from sys import argv


if __name__ == "__main__":
    value = {'email': argv[2]}
    data = par.urlencode(value)
    data = data.encode('ascii')
    requ = req.Request(argv[1], data)
    with req.urlopen(requ) as response:
        content = response.read()
        utf_cont = content.decode('utf-8')
        print(f"{utf_cont.strip()}")
