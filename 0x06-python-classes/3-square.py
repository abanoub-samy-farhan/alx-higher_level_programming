#!/usr/bin/python3
"""Here goes the first class"""


class Square:
    """Defines the class: Square"""
    def __init__(self, size=0):
        """Constructors
        Args:
            size: lenght of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Area of the Square
        Return:
            the size squared.
        """
        return self.__size ** 2
