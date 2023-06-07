#!/usr/bin/python3
for i in range(9):
    for j in range(i+1, 10):
        if int(str(i) + str(j)) != 89:
            print("{:02d}, ".format(i*10 + j), end="")
        else:
            print("{0}{1}".format(i, j))
