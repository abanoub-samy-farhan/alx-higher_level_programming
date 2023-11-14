#!/usr/bin/python3
"""making a good progress in the upcomming stage"""
from json import dumps, loads


class Base:
    """Class tha hava a base for everything"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructors of the class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Jsonifies a dict.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''Unjsonifies a dictionary.'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves jsonified object to file.'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w",
                  encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        '''Loads instance from dictionary.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new_shape = Rectangle(3, 4)
        elif cls is Square:
            new_shape = Square(5)
        else:
            new_shape = None
        new_shape.update(**dictionary)
        return new_shape

    @classmethod
    def load_from_file(cls):
        '''Loads string from file and unjsonifies.'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as file_s:
            return [cls.create(**d)
                    for d in cls.from_json_string(file_s.read())]
