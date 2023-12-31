#!/usr/bin/python3
"""Here goes the first class"""


class Square:
    """Defines the class: Square"""
    def __init__(self, size=0):
        """Constructors
        Args:
            size: lenght of the square.
        """
        self.size = size

    @property
    def size(self):
        """Size of the square
        Returns:
            the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Constructors
        Args:
            size: lenght of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of the square
        Returns:
            the area of the square
        """
        return self.__size ** 2
