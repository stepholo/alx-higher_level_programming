#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    A function that replaces element of a list at a specific position

    Parameters:
         my_list - list of elements
         idx - The index at which to do the replacement
         element - The element to replace at index idx

    Return:
       if idx < 0 or idx > index range of my_list return my_list
       else return the new list with the replaced value

    """
    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    else:
        my_list[idx] = element
        return my_list
