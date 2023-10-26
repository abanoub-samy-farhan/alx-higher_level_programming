#!/usr/bin/python3
"""here goes the code"""

class Square:
    """Defines the class: Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructors
        Args:
            size: lenght of the square.
            position: the position of the printed
        """
        self.size = size
        self.__position = position
 
    @property
    def size(self):
        """Size of the square
        Returns:
            the size of the square
        """
        return self.__size

    @property
    def position(self):
        """Position retraival for assignemnet"""
        return self.__positiion

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

    @position.setter
    def positon(self, value):
        """Setter of the position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__postion = value
    def area(self):
        """area of the square
        Returns:
            the area of the square
        """
        return self.__size ** 2
    def my_print(self):
        """my_print is a customized printing method
        prints # with the size of the square
        """
        if self.__size > 0:

            [print("") for empty in range(self.__position[1])]
            for j in range(self.__size):
                [print(" ", end='') for space in range(self.__position[0])]
                [print("#", end='') for hasx in range(self.__size)]
                [print()]
        else:
            print()
