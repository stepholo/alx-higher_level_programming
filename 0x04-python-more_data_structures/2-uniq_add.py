def uniq_add(my_list=[]):
    """ Adds all unique integers in a list (only once for each integer)

    Parameter:
      - my_list: The list

    Return:
     - The sum of the integers
    """
    a = sum(set(my_list))

    return a
