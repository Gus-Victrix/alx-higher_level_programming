#!/usr/bin/python3

"""Make requests using the requests module"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        q = ""
    else:
        q = sys.argv[1]

    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        responseDict = r.json()
        name = responseDict.get("name")
        idUser = responseDict.get("id")
        if idUser is None or name is None:
            print("No result")
        else:
            print("[{}] {}".format(idUser, name))
    except Exception:
        print("Not a valid JSON")
