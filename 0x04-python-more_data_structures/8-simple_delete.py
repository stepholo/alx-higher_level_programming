#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """ A function that deletes a key in a dictionary

    Parameter:
      - a_dictionary: The dictionary
      - key: the key to delete

    Return:
      - The dictionary without the key
    """
    a = list(a_dictionary)
    if key not in a:
        return a_dictionary
    elif key in a:
        del a_dictionary[key]
        return a_dictionary
