#!/usr/bin/python3
def best_score(a_dictionary):
    """ A function that returns keys with the biggest integer value

    Paramaters:
      - a_dictionary

    Return:
       - The key with the biggest integer else none
    """
    if a_dictionary is None:
        return
    else:
        keys = list(a_dictionary)
        max_key = keys[0]
        max_value = a_dictionary[max_key]

        for key in keys:
            if max_value < a_dictionary[key]:
                max_value = a_dictionary[key]
                max_key = key

        return max_key
