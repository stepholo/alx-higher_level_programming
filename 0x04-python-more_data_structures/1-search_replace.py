#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ Replaces all occurences of an element by another in a new list

    Parameter:
       - my_list: The list to check
       - search: the element to replace in the list
       - replace: is the new element

    Return:
       - a new list with the new values

    """
    new_list = [replace if x == search else x for x in my_list]

    return new_list
