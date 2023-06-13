#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    A function that returns the maximum integer of a list
    assuming the list contaings only integers

    Parameters:
       my_list: The containing the elements

    Return:
        The maximum integer  of my_list
    """
    if len(my_list) < 1:
        return
    else:
        ma_x = my_list[0]
        for i in my_list:
            if ma_x < i:
                ma_x = i
        return ma_x
