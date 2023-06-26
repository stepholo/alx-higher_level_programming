#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    A function that prints the first x elements of a list and only integers

    Parameter:
      my_list: The list containing elements
      x: The number of elements to print

    Return:
      The real number of integers printed
    """
    no_of_elements = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            no_of_elements += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print()
    return no_of_elements
