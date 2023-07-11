#!/usr/bin/python3
"""


Module to define to_json_string


"""


import json


def to_json_string(my_obj):
    """ A funtion that does JSON serialization

    Arg:
       my_obj: the object to turn to json data

    Return:
       json representation of an object (string)
    """
    char = json.dumps(my_obj)
    return char
