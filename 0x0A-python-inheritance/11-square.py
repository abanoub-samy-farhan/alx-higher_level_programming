#!/usr/bin/python3
"""returns another inherited lib"""
Rectangle = __import__("8-rectangle").Rectangle


class Square(Rectangle):
    """another inherited lib for another work"""
    def __init__(self, size):
        """defining the constructors of the project"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returning the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """returning a defining string for the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
