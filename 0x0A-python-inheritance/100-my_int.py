#!/usr/bin/python3
"""python is a good language"""


class MyInt(int):
    """int but has some cool stuff"""

    def __eq__(self, value):
        """returning the revarse of the normal function"""
        return super().__ne__(value)

    def __ne__(self, value):
        """returning the reverse value of it"""
        return super().__eq__(value)
