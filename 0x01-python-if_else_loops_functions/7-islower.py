#!/usr/bin/python3
def islowe(c):
    '''Checks for lowercase character'''

    if ord(c) >= 97 and ord(c) <= 127:
        return True
    else:
        return False
