#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Introduce a method """

    def __init__(self, size=0):
        """ Class Initialization

        Arg:
           size: the size of square
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Public instance method
        Return:
           The calculated area of square
        """
        return self.__size ** 2
