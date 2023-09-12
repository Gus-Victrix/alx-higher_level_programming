#!/usr/bin/python3

"""
Convert a json obj into python one
"""

import json


def from_json_string(my_obj):
    """
    Convert a json obj into python one
    """
    return json.loads(my_obj)
