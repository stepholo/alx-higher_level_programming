#!/usr/bin/python3
"""Defines a square"""


class Square:
    """ class instation"""
    def __init__(self, size=0):
        """ Class initialization handled with exeption

        Arg:
           size: The size of square
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
