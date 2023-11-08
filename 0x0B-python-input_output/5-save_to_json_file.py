#!/usr/bin/python3
"""defining the function"""


import json


def save_to_json_file(my_obj, filename):
    """returning the json file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
