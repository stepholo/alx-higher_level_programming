#!/usr/bin/python3
def is_same_class(obj, a_class):
    """checks for the instance of the object obj in a_class

    Arg:
       obj: object to check
       a_class: the class to check in

    Return:
       True if obj is of instance a_class otherwise False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
