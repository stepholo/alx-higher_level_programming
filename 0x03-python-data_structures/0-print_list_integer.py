#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    A function that prints content of a list

    Parameter:
     - my_list=[] - The list to get its content

    Return:
      - Prints content of the my_list assuming they are all integers

    """
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]), end="\n")
