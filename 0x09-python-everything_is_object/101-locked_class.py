#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    """
    Prevents any variable to be added in the class
    """
    def __init__(self):
        """Define the main and only instance"""
        self.first_name = None

    def __setattr__(self, name, value):
        """set attribute according to the allowed ones"""
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
