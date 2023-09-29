#!/usr/bin/python3
"""Module that defines a function for fetching url
"""


import urllib.request


def fetch_url(url):
    """Function that fetches a given url
    Param:
       url - the provided url
    Return:
       type, content and utf8
    """
    with urllib.request.urlopen(url) as response:
        contents = response.read()
        utf8_content = contents.decode('utf-8')
        print("Body response:")
        print(f"\t- type: {type(contents)}")
        print(f"\t- content: {contents}")
        print(f"\t- utf8 content: {utf8_content}")


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_url(url)
