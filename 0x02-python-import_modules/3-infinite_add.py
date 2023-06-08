#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argument = []
    arg_ment = sys.argv
    sum = 0

    if len(arg_ment) == 1:
        sum = 0

    else:
        for i in range(1, len(arg_ment)):
            argument.append(int(arg_ment[i]))

        for i in range(len(argument)):
            sum += argument[i]

    print(sum)
