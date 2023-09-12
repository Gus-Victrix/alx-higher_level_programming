#!/usr/bin/python3

"""
Read a json file an convert it into python obj
"""

import json


def load_from_json_file(filename):
    """
    Read a json file an convert it into python obj
    """
    with open(filename, "r", encoding="utf-8") as fl:
        return json.load(fl)
