#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{0} is {pve}". format(number, pve = "positive"))
elif number < 0:
    print("{0} is {nve}". format(number, nve = "negative"))
elif number == 0:
    print("{0} is {nll}". format(number, nll = "zero"))
