#!/usr/bin/python3
"""module to define class for testing rectangle validation"""


import unittest
from unittest import mock
from io import StringIO
from models.rectangle import Rectangle


class TestValidateAttribute(unittest.TestCase):
    """class that validates the attributes of class Rectangle"""

    def test_width(self):
        """method to test width attribute"""
        rect = Rectangle(10, 2)
        self.assertEqual(rect.width, 10)
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
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 3, 0, -4)
            rect.height
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 4, 5, '39')
            rect.height

    def test_area(self):
        """method to test the area"""
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)
        with self.assertRaises(ValueError):
            rect = Rectangle(4, -3)
            rect.area()
        with self.assertRaises(TypeError):
            rect = Rectangle([4], 2)
            rect.area()

    def test_display(self):
        """method to test the diplay"""
        rect = Rectangle(2, 3)
        expected_output = '##\n##\n##\n'
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            rect.display()
            actual_output = stdout.getvalue()
        self.assertEqual(actual_output, expected_output)
        with self.assertRaises(ValueError):
            rect = Rectangle(-2, 3)
            rect.display()
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 'list')
            rect.display()


if __name__ == '__main__':
    unittest.main()
