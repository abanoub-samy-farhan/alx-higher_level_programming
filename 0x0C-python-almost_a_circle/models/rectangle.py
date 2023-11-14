#!/usr/bin/python3
'''the functions is very well prepared'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''returning the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''y of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, directions=True):
        '''Method for validating the value.'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if directions and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not directions and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """returning the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """returning the shape of the function"""
        string = ("#" * self.__width + '\n') * self.__height
        print(string, end='')
