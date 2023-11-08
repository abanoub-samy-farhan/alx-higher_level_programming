#!/usr/bin/python3
"""defining the function in the place"""


def load_from_json_file(filename):
    """returning the file json"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
