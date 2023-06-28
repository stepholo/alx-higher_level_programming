#!/usr/bin/python3
""" Defines a square"""


class Square:
    """Using property and setters"""

    def __init__(self, size=0):
        """Class initializer done with private instance attribute
        Arg:
           size: Private instance attribute
        """
        self.__size = size

    @property
    def size(self):
        """ Property to retrive size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property to set value for size
        Arg:
           value: the value of size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
