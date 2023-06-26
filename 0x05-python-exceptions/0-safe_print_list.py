#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ A function that prints x elements of a list
    Parameter:
       my_list: Contains list element
       x: The number of elements to be printed
    Return:
       The real number of elements printed
    """
    no_of_elements = 0
    for i in range(x):
        try:
            print(f'{my_list[i]}', end="")
            no_of_elements += 1
        except IndexError:
            break
    print()
    return no_of_elements
