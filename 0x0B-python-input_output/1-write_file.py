#!/usr/bin/python3
"""defining a funciton"""


def write_file(filename="", text=""):
    """returns the text in the file"""
    with open(filname, "w", encoding="utf-8") as f:
        return f.write(text)
