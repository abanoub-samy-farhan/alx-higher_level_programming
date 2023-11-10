#!/usr/bin/python3
""" file to be inputed and checked for direct and indirect inheritance"""


def inherits_from(obj, a_class):
    """returning True on sucsses, and False on failure"""
    return isinstance(obj, a_class) and type(obj) != a_class
