#!/usr/bin/python3
"""definging the following thing as it is"""


def class_to_json(obj):
    """returns the dictionary of the object"""
    return obj.__dict__
