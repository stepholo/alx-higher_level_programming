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
        rect = Rectangle(2, 3, 2, 2)
        expect = '\n\n  ##\n  ##\n  ##\n'
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            rect.display()
            actual = stdout.getvalue()
        self.assertEqual(actual, expect)
        with self.assertRaises(ValueError):
            rect = Rectangle(-2, 3)
            rect.display()
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 'list')
            rect.display()

    def test_str(self):
        """method to test string representation"""
        rect = Rectangle(2, 3, 2, 1, 12)
        expect = '[Rectangle] (12) 2/1 - 2/3\n'
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(rect)
            actual = stdout.getvalue()
        self.assertEqual(expect, actual)
        rect = Rectangle(5, 5, 1)
        no = rect.id
        expect1 = f'[Rectangle] ({no}) 1/0 - 5/5\n'
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(rect)
            actual1 = stdout.getvalue()
        self.assertEqual(expect1, actual1)
        with self.assertRaises(ValueError):
            rect = Rectangle(-2, 3, -1, 0)
            print(rect)
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 's', 1, '0')
            print(rect)

    def test_update(self):
        """method to test the update function of the class rectangle"""
        rect = Rectangle(10, 10, 10, 10)
        expected = '[Rectangle] (89) 4/5 - 2/3\n'
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            rect.update(89, 2, 3, 4, 5)
            print(rect)
            actual = stdout.getvalue()
        self.assertEqual(expected, actual)
        expected = '[Rectangle] (89) 1/3 - 4/2\n'
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            rect.update(x=1, height=2, y=3, width=4, id=89)
            print(rect)
            actual = stdout.getvalue()
        self.assertEqual(expected, actual)
        with self.assertRaises(ValueError):
            rect.update(3, -1, 4, 9)
            print(rect)
        with self.assertRaises(TypeError):
            rect.update(5, '1', '4', 9)
            print(rect)
        with self.assertRaises(ValueError):
            rect.update(x=-1, height=2, y=-3, width=4)
            print(rect)
        with self.assertRaises(TypeError):
            rect.update(x=1, height=[2], y=3, width='4')
            print(rect)


if __name__ == '__main__':
    unittest.main()
