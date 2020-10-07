#!/usr/bin/python3
"""a function that reads a file"""


def read_file(filename=""):
    """Reads a text file and prints it
    filename: Filename
    """

    with open(filename, mode="r", encoding='utf-8') as my_file:
    	for line in file:
            print(line,end="")
