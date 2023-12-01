#!/usr/bin/python3

"""Make requests using the requests module"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
                                                                sys.argv[2],
                                                                sys.argv[1]))
    count = 0
    for commit in r.json():
        if count > 9:
            break
        print("{}: {}".format(
                        commit.get("sha"),
                        commit.get("commit").get("author").get("name")))
        count += 1
