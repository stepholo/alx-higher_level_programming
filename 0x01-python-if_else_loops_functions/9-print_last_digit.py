#!/usr/bin/python3
def print_last_digit(number):
    ''' Prints or returns the last digit of a number

    Arg:
       number - number to get its last digit

    Return:
         Return or prints the last digit of the number
    '''
    print("{}".format(abs(number) % 10), end="")
    return (abs(number) % 10)
