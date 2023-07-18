#!/usr/bin/python3
"""module to define class for testing Square class"""


import unittest
from unittest import mock
from io import StringIO
from models.square import Square


class TestValidateAttribute(unittest.TestCase):
    """Class that validate the attribues and methods of class Square"""

    def test_str(self):
        """method to test string representation of object"""
        squa = Square(3, 1, 3)
        no = squa.id
        expected = f'[Square] ({no}) 1/3 - 3\n'
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(squa)
            actual = stdout.getvalue()
        self.assertEqual(expected, actual)
        with self.assertRaises(ValueError):
            squa = Square(-2, 3, 4)
            print(squa)
        with self.assertRaises(TypeError):
            squa = Square(2, '3', 4)
            print(squa)

    def test_get_set(self):
        """method to test the getter and setter of the class square"""
        squa = Square(5)
        no = squa.id
        expected = f'[Square] ({no}) 0/0 - 5\n'
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(squa)
            actual = stdout.getvalue()
        with self.assertRaises(TypeError):
            squa.size = '9'
            print(squa)
        with self.assertRaises(ValueError):
            squa.size = -4
            print(squa)

    def test_update(self):
        """method to test square update method"""
        squa = Square(5)
        expected = '[Square] (1) 3/4 - 2\n'
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            squa.update(1, 2, 3, 4)
            print(squa)
            actual = stdout.getvalue()
        self.assertEqual(expected, actual)
        squa.update(size=7, id=89, y=1)
        expected = '[Square] (89) 3/1 - 7\n'
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(squa)
            actual = stdout.getvalue()
        self.assertEqual(expected, actual)
        with self.assertRaises(TypeError):
            squa.update(size='7', id=89, y=1)
            squa.update(1, 2.0, 3, 4)
        with self.assertRaises(ValueError):
            squa.update(1, 2, -3, 4)
            squa.update(size=-7, id=89, y=1)

    def test_dictionary(self):
        """method to test dictionary representation"""
        rect = Square(10, 2, 1)
        expected = str(rect.to_dictionary()) + '\n'
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            rect_1 = rect.to_dictionary()
            print(rect_1)
            actual = stdout.getvalue()
        self.assertEqual(expected, actual)
        rect2 = Square(1, 1)
        rect2.update(**rect_1)
        no = rect2.id
        expected = f'[Square] ({no}) 2/1 - 10\n'
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(rect2)
            actual = stdout.getvalue()
        self.assertEqual(expected, actual)
        self.assertFalse(rect == rect2)
        with self.assertRaises(ValueError):
            dicti = {'x': 1, 'y': 9, 'id': 1, 'size': -10}
            rect.update(**dicti)
        with self.assertRaises(TypeError):
            dicti = {'x': 1, 'y': [9], 'id': 1, 'size': 10}
            rect.update(**dicti)


if __name__ == '__main__':
    unittest.main()
