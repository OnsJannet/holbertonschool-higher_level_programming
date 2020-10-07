#!/usr/bin/python3
"""
a function that returns the number
of lines of a text file
"""


def number_of_lines(filename=""):
"""a fucntion that returns line numbers
"""
    with open(filename) as my_file:
        lines = len(my_file.readlines())
    return lines
