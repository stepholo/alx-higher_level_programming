#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("{0}{1}".format(0, i), end=", ")
    else:
        if i < 99:
            print(i, end=", ")
        else:
            print(i)
