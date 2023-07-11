#!/usr/bin/python3
"""


Module to define save_to_json_file


"""

import json


def save_to_json_file(my_obj, filename):
    """Serializes an object and saves in a file

    Arg:
       my_obj: object to serialize
       filenmae: the file to save into

    Return:
       A .json file
    """
    char = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as f:
        no = f.write(char)

    return no
