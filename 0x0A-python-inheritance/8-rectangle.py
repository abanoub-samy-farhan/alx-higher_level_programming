#!/usr/bin/python3
"""inherits the shape and advance the project"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """defining the variables of the rectangle"""
        integer_validator("height", height)
        integer_validator("width", width)
        self.__height = height
        self.__width = width
