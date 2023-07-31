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

    def area(self):
        """Implement the area method that finds the area"""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representationof the class Rectangle"""
        return f'[Rectangle] {self.__width}/{self.__height}'
