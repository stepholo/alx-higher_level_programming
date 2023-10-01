#!/usr/bin/python3
"""Module Write a Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API to display your id
    You must use Basic Authentication with a personal access token as
    password to access to your information
    (only read:user permission is needed)
"""

import requests
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    auth = (username, password)
    url = 'https://api.github.com/user'
    try:
        r = requests.get(url, auth=auth)
        r_json = r.json()
        if 'id' in r_json:
            output = f"{r_json['id']}"
            print(output)
        else:
            print(None)
    except Exception:
        print(None)
