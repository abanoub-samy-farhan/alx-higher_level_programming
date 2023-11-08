#!/usr/bin/python3
"""defining the function in the place"""


import json


def load_from_json_file(filename):
    """returning the file json"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
