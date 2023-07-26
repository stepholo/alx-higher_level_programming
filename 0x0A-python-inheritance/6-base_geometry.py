#!/usr/bin/python3
"""


Defines an BaseGeometry


"""


class BaseGeometry:
    """defines BaseGeometry class

    Attributes:
       area: method that raises an exception
    """

    def area(self):
        """method to raise error message"""
        raise Exception('area() is not implemented')
