#!/usr/bin/python3
"""


Module to define is_kind_of_class


"""


def is_kind_of_class(obj, a_class):
    """checks the instance of an object in a class

    Arg:
       obj; the object to check
       a_class: The class to check in
    Returns:
       True if obj in a_class otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
