def new_in_list(my_list, idx, element):
    """
    A function that replaces the an element at at specific index

    Parameter:
      - my_list - The list
      - idx - index
      - element - the element to replace at index idx in list my_list

    Return:
     - New list with the changed element
    """
    new_list = my_list[:]
    if idx < 0:
        return new_list
    elif idx > (len(new_list) - 1):
        return new_list
    else:
        new_list[idx] = element

    return new_list
