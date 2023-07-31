#!/usr/bin/python3
"""

Defines class Rectangle that inherits from class BaseGeometry


"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines Rectangle class

    Attributes:
      width: private attribute defining width of rectangle
      height: private attribute defining height of rectangle
    """

    def __init__(self, width, height):
        """class instantiation"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
