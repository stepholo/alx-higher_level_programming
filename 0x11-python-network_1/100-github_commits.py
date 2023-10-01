#!/usr/bin/python3
""" Module that list 10 commits (from the most recent to oldest)
    of the repository “rails” by the user “rails”
    You must use the GitHub API, here is the documentation
    https://developer.github.com/v3/repos/commits/
    Print all commits by: `<sha>: <author name>` (one by line)
"""

import requests
from sys import argv


if __name__ == "__main__":
    name = argv[1]
    owner = argv[2]
    url = f"https://api.github.com/repos/{owner}/{name}/commits"

    r = requests.get(url)
    r_json = r.json()

    if isinstance(r_json, list) and len(r_json) > 0:
        for commit in r_json[:10]:
            sha = commit['sha']
            auth_name = commit['commit']['author']['name']
            print(f"{sha} {auth_name}")
    else:
        print('No commits found')
