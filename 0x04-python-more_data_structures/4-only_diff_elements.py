#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """ Returns a set of all elements present in only one set

    Parameter:
      - set_1: the first set
      - set_2: the second set

    Return:
       - all elements present in only one set
    """
    return list(set_1 ^ set_2)
