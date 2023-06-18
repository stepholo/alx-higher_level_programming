#!/usr/bin/python3
''' A program that prints z - a but interchanged with Z - A '''
for i in range(ord('z'), ord('a'), -2):
    print("{}{}".format(chr(i), (chr(i - 1)).upper()), end="")
