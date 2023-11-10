#!/usr/bin/python3
""" file git into the bases of the geometry """


class BaseGeometry:
    """ a class that do sth i don't know yet"""

    def area(self):
        """ not yet done to receive anything """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """returning an validation for the data provided

        Constructors:
        Args:
            name: the name of the variable to validate
            value: the value that would be assigned into it, must be integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
