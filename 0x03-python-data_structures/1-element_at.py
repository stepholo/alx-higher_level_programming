#!/usr/bin/python3
def element_at(my_list, idx):
    """
    A function that retrieves an element of a list

    Parameter:
     - my_list: the list containing elements to be retrived
     - idx = The index of the element to be retrieved

    Return:
          if idx < 0 return None
          if idx > range of my_list return None
    """
    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
    else:
        return my_list[idx]
