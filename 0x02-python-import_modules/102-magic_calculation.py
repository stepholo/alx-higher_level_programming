#!/usr/bin/python3
def magic_calculation(a, b):
    '''Match bytecode provided

    Arg:
       a - First operand
       b - Second operand

    Return:
          Addition or subtraction
   '''

    from magic_calculation_102 import add sub

    if a < b:
        c = add(a, b)

        for i in range(4, 6):
            c = c + i
        return c

    else:
        return sub(a, b)
        
