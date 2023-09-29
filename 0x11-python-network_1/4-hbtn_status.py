#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status
    using the package requests
"""

import requests


if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content {r.content}")
