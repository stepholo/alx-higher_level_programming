#!/usr/bin/python3
import sys


def print_art():
    art = "and that piece of art is useful - Dora Korpar, 2015-10-19"
    sys.stderr.write(art + '\n')
    sys.exit(1)


print_art()
