#!/usr/bin/python3
def number_of_lines(filename=""):
    """
    a function that returns the number
    of lines of a text file
    """
    lines = 0
    with open(filename, 'r', encoding='utf-8') as my_file:
        for n_line in my_file:
            n_lines += 1
    return n_lines
