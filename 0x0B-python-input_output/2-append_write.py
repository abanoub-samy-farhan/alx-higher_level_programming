#!/usr/bin/python3
"""defining the function"""


def append_write(filename="", text=""):
    """returning the appended text in the file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
