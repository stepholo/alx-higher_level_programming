#!/usr/bin/python3
"""

Defines MyList module


"""


class MyList(list):
    """MyList inherits from list type
    Defines a method that sorts the list created

    Raise:
     ValuError: if the method is used with a value not int type
    """

    def print_sorted(self):
        """define a method to sort the list created"""
        sorted_list = sorted(self)
        print(sorted_list)
