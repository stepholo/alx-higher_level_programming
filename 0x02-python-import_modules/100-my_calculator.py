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
        operator = argument[2]

        if operator not in ['+', '-', '*', '/']:
            print("Unknown operator. Available operator: +, -, * and /")
            sys.exit(1)

        if operator == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif operator == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif operator == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif operator == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
