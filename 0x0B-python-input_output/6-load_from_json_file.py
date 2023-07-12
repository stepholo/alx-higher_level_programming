#!/usr/bin/python3
"""


Module to define load_from_json_file


"""

import json


def load_from_json_file(filename):
    """Serializes an object and saves in a file

    Arg:
       filenmae: the file containing object to deserialize

    Return:
       A python object
    """
    with open(filename, "r", encoding="utf-8") as f:
        char = f.read()
        create = json.loads(char)

    return create
