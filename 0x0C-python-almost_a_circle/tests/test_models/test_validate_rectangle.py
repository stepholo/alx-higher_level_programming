#!/usr/bin/python3
"""module to define class for testing rectangle validation"""


import unittest
from models.rectangle import Rectangle


class TestValidateAttribute(unittest.TestCase):
    """class that validates the attributes of class Rectangle"""

    def test_width(self):
        """method to test width attribute"""
        rect = Rectangle(10, 2)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.id, 4)
        with self.assertRaises(ValueError):
            rect = Rectangle(-1, 10)
            rect.width
        with self.assertRaises(TypeError):
            rect = Rectangle('10', 2)
            rect.width

    def test_height(self):
        """method to test height attribute"""
        rect = Rectangle(10, 10)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.id, 1)
        with self.assertRaises(ValueError):
            rect = Rectangle(2, -3)
            rect.height
        with self.assertRaises(TypeError):
            rect = Rectangle(2, [1])
            rect.height

    def test_x(self):
        """method to test keyword x"""
        rect = Rectangle(10, 2, 1)
        self.assertEqual(rect.x, 1)
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 3, -1)
            rect.x
            self.assertEqual(rect.id, 1)
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 4, '4')
            rect.x

    def test_y(self):
        """method to test keyword y"""
        rect = Rectangle(2, 3, 4, 2)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 10)
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 3, 0, -4)
            rect.height
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 4, 5, '39')
            rect.height
            self.assertEqual(rect.id, 1)
