#!/usr/bin/python3
"""Module to define class Base
"""


class Base:
    """Parent class to manage id attribute in all classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor
        Parameter:
            id: class attribute that returns object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
