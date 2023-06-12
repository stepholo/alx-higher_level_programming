#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    A function that prints the list in reverse

    Parameters:
       - my_list - The list to be reversed

    Return:
       - The reversed list

    """
    i = (len(my_list)) - 1
    while i >= 0:
        print("{:d}".format(my_list[i]))
        i -= 1
