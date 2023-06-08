#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argument = sys.argv
    j = len(argument) - 1

    if len(argument) == 1:
        print(f"{0:d} arguments.")
    elif len(argument) == 2:
        print(f"{1:d} argument:")
        print("{}: {}".format((len(argument) - 1), argument[1]))
    else:
        print("{} arguments:".format(j))
        for i in range(1, len(argument)):
            print("{}: {}".format(i, argument[i]))
