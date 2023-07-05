#!/usr/bin/python3


""" Defines a rectangle """


class Rectangle:
    """Class rectangel
    Arg:
      width: width of the rectangle
      height: height of the rectangle
    Raise:
      TypeError: is either of sides is not and int
      ValueError: if either of the sides is less than 0
    """
    def __init__(self, width=0, height=0):
        """Class initialization"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the value of the width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)
