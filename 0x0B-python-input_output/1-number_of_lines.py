#!/usr/bin/python3
def number_of_lines(filename=""):
    """
    a function that returns the number
    of lines of a text file
    """
    n_line = 0
    with open(filename) as my_file:
        lines = len(my_file.readlines())
    return lines

