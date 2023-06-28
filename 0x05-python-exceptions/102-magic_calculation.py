#!/usr/bin/python3
def magic_calculation(a, b):
    """Code that does just like Bytecode"""
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except Exception as e:
            result += a + b
            break
    return result
