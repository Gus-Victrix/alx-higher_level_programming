#!/usr/bin/python3

"""Make requests using the requests module"""

import requests
import sys

if __name__ == "__main__":
    infos = {"email": sys.argv[2]}
    r = requests.post(sys.argv[1], data=infos)
    print(r.text)
