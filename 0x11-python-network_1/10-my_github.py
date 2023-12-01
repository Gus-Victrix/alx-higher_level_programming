#!/usr/bin/python3

"""Make requests using the requests module"""

import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(user, pwd))
    print(r.json().get("id"))
