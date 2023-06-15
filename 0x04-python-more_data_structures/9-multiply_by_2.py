#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """ Multiplies all values of a dictionary assuming there are integers

    Parameter:
      - a_dictionary

    Return:
     - A new dictionary with all the values multiplied by 2
    """
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict
