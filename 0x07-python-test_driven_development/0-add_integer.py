#!/usr/bin/python3
"""

This module is a function that adds two integer

"""
def add_integer(a, b=98):
    """ Adds two integers
    Arg:
       a: First integer
       b: Second integer. 98 by default
    Return:
       the sum of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
