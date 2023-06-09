#!/usr/bin/python3
def islower(c):
    '''Checks if the letter 'c' is lowercase

    Arg:
       c - check whether its lowercase

    Return:
          If c is lowercase return true
          else return false
    '''
    letter = ord(c)

    if 97 <= letter <= 122:
        return True
    else:
        return False
