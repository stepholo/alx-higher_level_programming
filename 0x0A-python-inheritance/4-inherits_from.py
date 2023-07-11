#!/usr/bin/python3
"""


Module to define inherits _from function


"""


def inherits_from(obj, a_class):
    """using issubclass to check for inheritance
    Arg:
       obj: object to be checked
       a_class: to to check in
    Return:
       True if obj if inherited from a_class else False
    """
    obj_classes = type(obj).__mro__[1:]

    return any(a_class is cls for cls in obj_classes)
