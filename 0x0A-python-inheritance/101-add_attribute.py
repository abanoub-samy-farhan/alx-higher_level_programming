#!/usr/bin/python3
"""final final final final final final final"""


def add_attribute(obj, name, value):
    """add values to objects"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
