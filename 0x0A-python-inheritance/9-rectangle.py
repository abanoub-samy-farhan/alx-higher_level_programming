#!/usr/bin/python3
'''Module for Rectangle class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A subclass representing a rectangle.'''
    def __init__(self, width, height):
        '''Constructor of the class with privte instances.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returning the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """returns the description of the class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
