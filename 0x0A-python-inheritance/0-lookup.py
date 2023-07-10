#!/usr/bin/python3
def lookup(obj):
    """ A function that returns the list of available
        attributes and methods of an object

    Arg:
      obj: The object to get its attributes

    Return:
      A list object containing the attributes of the object obj
    """
    return dir(obj)
