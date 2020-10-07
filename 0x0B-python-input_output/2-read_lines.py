#!/usr/bin/python3
"""a function that reads n lines of a file"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines and prints it to stdout
    filename: Filename
    """

    with open(filename, mode="r", encoding='utf-8') as my_file:
        if nb_lines <= 0:
            for line in my_file:
                print(line, end="")
        else:
            for line in range(nb_lines):
                print(my_file.readline(), end="")
