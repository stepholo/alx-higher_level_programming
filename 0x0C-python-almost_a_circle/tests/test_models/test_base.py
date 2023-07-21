"""Modules for unit testing using unittest"""


import unittest
import os
from unittest import mock
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """class to test the base class"""

    def test_empty_arg(self):
        """method to test when object has no argument"""

        base = Base()
        no = base.id
        self.assertEqual(base.id, no)
        base = Base()
        no = base.id
        self.assertEqual(base.id, no)
        base = Base()
        no = base.id
        self.assertEqual(base.id, no)

    def test_with_arg(self):
        """method to test when object has argument"""

        base1 = Base()
        no = base1.id
        self.assertEqual(base1.id, no)
        base1 = Base(12)
        self.assertEqual(base1.id, 12)
        base1 = Base()
        no = base1.id
        self.assertEqual(base1.id, no)
        base1 = Base(2)
        self.assertEqual(base1.id, 2)
        base1 = Base()
        no = base1.id
        self.assertEqual(base1.id, no)

    def test_with_invalid_arg(self):
        """method to test when object has other data types"""

        base = Base('1')
        self.assertEqual(base.id, '1')
        base = Base([1, 3, 4])
        self.assertEqual(base.id, [1, 3, 4])

    def test_to_json_string(self):
        """method to test json conversion"""
        rect = Rectangle(10, 7, 2, 8)
        dicti = rect.to_dictionary()
        self.assertTrue(type(dicti) == dict)
        json_str = Base.to_json_string([dicti])
        self.assertTrue(type(json_str) == str)
        expected = '[{"id": 15, "width": 10, "height": 7, "x": 2, "y": 8}]\n'
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(json_str)
            actual = stdout.getvalue()
        self.assertEqual(expected, actual)
        json_str = Base.to_json_string(None)
        self.assertTrue(json_str == '[]')
        json_str = Base.to_json_string([])
        self.assertTrue(json_str == '[]')

    def test_save_to_file(self):
        """method to test if json repr is being saved in to a file"""
        if os.path.exists('Rectangle.json'):
            os.remove('Rectangle.json')
        rect = Rectangle(10, 7, 2, 8)
        rect1 = Rectangle(2, 4)
        Rectangle.save_to_file([rect, rect1])
        self.assertTrue(os.path.exists('Rectangle.json'))
        with open('Rectangle.json', 'r') as f:
            char = f.read()
        self.assertTrue(type(char) == str)

    def test_json_from_string(self):
        """method to test deserialization"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(list_input) == list)
        self.assertTrue(type(json_list_input) == str)
        self.assertTrue(type(list_output) == list)

    def test_create(self):
        """method to test the class method create"""
        rect = Rectangle(3, 5, 1)
        dicti = rect.to_dictionary()
        rect2 = Rectangle.create(**dicti)
        expected = '[Rectangle] (1) 1/0 - 3/5\n'
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(rect2)
            actual = stdout.getvalue()
        self.assertEqual(expected, actual)
        self.assertFalse(rect is rect2)
        self.assertFalse(rect == rect2)

    def test_load_from_file(self):
        """method to test load from file class method"""
        if os.path.exists('Rectangle.json'):
            os.remove('Rectangle.json')
        none_output = Rectangle.load_from_file()
        self.assertTrue(isinstance(none_output, list))
        rect = Rectangle(10, 7, 2, 8)
        rect1 = Rectangle(2, 4)
        Rectangle.save_to_file([rect, rect1])
        self.assertTrue(os.path.exists('Rectangle.json'))
        list_rec_output = Rectangle.load_from_file()
        self.assertTrue(isinstance(list_rec_output, list))
        for inst in list_rec_output:
            self.assertTrue(isinstance(inst, Rectangle))

    def test_save_to_file_csv(self):
        """method to test saving instance attributes to a csv file"""
        if os.path.exists('Rectangle.csv'):
            os.remove('Rectangle.csv')
        Rectangle.save_to_file_csv(None)
        self.assertTrue(os.path.exists('Rectangle.csv'))
        with open('Rectangle.csv', 'r') as f:
            char = f.read()
        self.assertTrue(isinstance(char, str))
        rect = Rectangle(10, 7, 2, 8)
        rect1 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([rect, rect1])
        self.assertTrue(os.path.exists('Rectangle.csv'))

    def test_load_from_file_csv(self):
        """method to test load instance attributes from a csv file"""
        if os.path.exists('Square.csv'):
            os.remove('Square.csv')
        sq1 = Square(5)
        sq2 = Square(7, 9, 1)
        Square.save_to_file_csv([sq1, sq2])
        self.assertTrue(os.path.exists('Square.csv'))
        csv_output = Square.load_from_file_csv()
        self.assertTrue(isinstance(csv_output, list))
        for inst in csv_output:
            self.assertTrue(isinstance(inst, Square))


if __name__ == '__main__':
    unittest.main()
