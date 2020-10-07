#!/usr/bin/python3
def read_file(filename=""):
    """Reads a text file and prints it
    filename: Filename
    """
    with open(filename, encoding='UTF8') as my_file:
        print(my_file.read(), end="")
