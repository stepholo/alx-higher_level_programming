#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import *

    argument = sys.argv
    if len(argument) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    else:
        a = int(argument[1])
        b = int(argument[3])

        if argument[2] != ('+' or '-' or '*' or '/'):
            print("Unknown operator. Available operator: +, -, * and /")
            sys.exit(1)

        else:
            for i in range(1, len(argument)):
                if argument[i] == '+':
                    print("{} {} {} = {}".format(a, argument[2], b, add(a, b)))
                elif argument[i] == '-':
                    print("{} {} {} = {}".format(a, argument[2], b, sub(a, b)))
                elif argument[i] == '*':
                    print("{} {} {} = {}".format(a, argument[2], b, mul(a, b)))
                elif argument[i] == '/':
                    print("{} {} {} = {}".format(a, argument[2], b, div(a, b)))
