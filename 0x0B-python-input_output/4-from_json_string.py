#!/usr/bin/python3
"""


Module to define from_json_string


"""


import json


def from_json_string(my_str):
    """ A funtion that does JSON deserialization

    Arg:
       my_str: the object to turn to Python data structure

    Return:
       an object of python data structure
    """
    char = json.loads(my_str)
    return char
