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
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attr:
                my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
        """returning a very specific code that make something"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
