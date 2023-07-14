#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A class that defines the test cases for a function"""

    def test_space(self):
        """Method to test for lack of comma or extra spaces
           in the list
        """
        self.assertEqual(max_integer([1,  2,     3,  5, 6, 7]), 7)

    def test_integers(self):
        """Method to test list containg only integers"""
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([1, 5, 3, 4]), 5)

    def test_float(self):
        """Method to test list containing integers and floats"""
        _pve = float('inf')
        _nve = float('-inf')
        self.assertEqual(max_integer([1.2, 1.3, 1.4, 1.5]), 1.5)
        self.assertEqual(max_integer([1, 0.9, 1.1, 3, 4]), 4)
        self.assertEqual(max_integer([_pve, _nve, 10]), _pve)

    def test_complex(self):
        """Method to test list containing complex numbers and integers"""
        with self.assertRaises(TypeError):
            max_integer([1+2j, 3+2j, 4+2j])
            max_integer([1+2j, 3.4, 100])

    def test_sting(self):
        """Method to test list containing string and integers"""
        with self.assertRaises(TypeError):
            max_integer(['r', '4', '3', 'school'])
            max_integer(['1', '2', 3, '4'])
            max_integer([2, 3, '1'])

    def test_other_type(self):
        """Method to test list containing other data types and integers"""
        self.assertEqual(max_integer([[1, 2], [1, 2, 3]]), [1, 2, 3])
        with self.assertRaises(TypeError):
            max_integer([[1, 2, 4, 5], 5])
            max_integer([(1, 3), [1, 2, 4]])
            max_integer([None, 4, 5])


if __name__ == '__main__':
    unittest.main()
