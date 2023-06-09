#!/usr/bin/python3
def uppercase(str):
    ''' Converts the str to uppercase

    Arg:
       str - string to be converted to uppercase

    Return:
          The uppercase version of the str
    '''
    new_str = ""
    for letter in str:
        if 97 <= ord(letter) <= 122:
            new_letter = chr(ord(letter) - 32)
        else:
            new_letter = letter

        new_str += new_letter

    print("{}".format(new_str))
