#!/usr/bin/python3
"""defining the file of the students"""


class Student:
    """class contaning the name of the fiel"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns json dict"""
        return self.__dict__
