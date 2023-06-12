#!/usr/bin/python3
def no_c(my_string):
    """
    A function that removes 'c' from my_string

    Parameter:
      - my_string - the string to check 

    Return:
      - The string without the letter 'c'
    """
    new_string = ""
    for i in my_string:
        if i.lower() != 'c':
            new_string += i

    return new_string
