#!/usr/bin/python3
"""Module to define class Square"""


import unittest
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method that returns string representation of square"""
        x = self.x
        y = self.y
        size = self.width
        return f"[Square] ({self.id}) {x}/{y} - {size}"
