"""Modules for unit testing using unittest"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """class to test the base class"""

    def test_empty_arg(self):
        """method to test when object has no argument"""

        base = Base()
        self.assertEqual(base.id, 1)
        base = Base()
        self.assertEqual(base.id, 2)
        base = Base()
        self.assertEqual(base.id, 3)

    def test_with_arg(self):
        """method to test when object has argument"""

        base1 = Base()
        self.assertEqual(base1.id, 4)
        base1 = Base(12)
        self.assertEqual(base1.id, 12)
        base1 = Base()
        self.assertEqual(base1.id, 5)
        base1 = Base(2)
        self.assertEqual(base1.id, 2)
        base1 = Base()
        self.assertEqual(base1.id, 6)

    def test_with_invalid_arg(self):
        """method to test when object has other data types"""

        base = Base('1')
        self.assertEqual(base.id, '1')
        base = Base([1, 3, 4])
        self.assertEqual(base.id, [1, 3, 4])


if __name__ == '__main__':
    unittest.main()
