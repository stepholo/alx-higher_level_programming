#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """ A function that replaces or adds key/value in a dictionary

    Parameter:
      - a_dictionary: The dictionary
      - key: key to add if not present
      - value: The value to overwrite if key is present

    Return:
      -  The final dictionary
    """
    a = list(a_dictionary)
    if key not in a:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value

    return a_dictionary
