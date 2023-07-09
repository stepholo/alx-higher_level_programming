#!/usr/bin/python3


"""Defines a rectangle"""


class Rectangle:
    """class rectangle
    arg:
       width: represents the width of the rectangle
       height: represents the height of the rectangle
    Raise:
       TypeError if measurement is not in integer
       ValueError if measurement is less than zero
    """
    def __init__(self, width=0, height=0):
        """Class initialization"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width value"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height value"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of the rectangle"""
        if self.__width == 0:
            perimeter = 0
        elif self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        """user friendly string representation of the rectangle"""
        rect = ""
        if self.__width == 0:
            return rect
        elif self.__height == 0:
            return rect
        else:
            for i in range(self.__height):
                if i < self.__height - 1:
                    rect += f"{'#' * self.__width}\n"
                else:
                    rect += f"{'#' * self.__width}"
            return rect

    def __repr__(self):
        """unambigous string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
