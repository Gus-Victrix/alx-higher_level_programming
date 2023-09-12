#!/usr/bin/python3

"""
Save a obj into json file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Save a obj into json file
    """
    with open(filename, "w", encoding="utf-8") as fl:
        json.dump(my_obj, fl)
