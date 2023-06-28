#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Defined by private instance attribure"""

    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            i = 1
            while i <= self.__size:
                print("{}".format('#' * self.__size))
                i += 1
