#!/usr/bin/python3
"""making a good progress in the upcomming stage"""


class Base:
    """Class tha hava a base for everything"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructors of the class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb.objects
