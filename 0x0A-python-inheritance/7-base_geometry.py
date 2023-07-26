#!/usr/bin/python3
"""


Defines an BaseGeometry


"""


class BaseGeometry:
    """defines BaseGeometry class

    Attributes:
       area: method that raises an exception
       integer_validator: method that validates value
    """

    def area(self):
        """method to raise error message"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """method that validates the integer value"""
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')
