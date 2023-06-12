#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    A function that prints the list in reverse

    Parameters:
       - my_list - The list to be reversed

    Return:
       - The reversed list

    """
    new_list = my_list[::-1]
    for i in new_list:
        print("{:d}".format(i))
