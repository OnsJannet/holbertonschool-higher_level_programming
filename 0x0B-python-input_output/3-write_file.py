#!/usr/bin/python3
"""a function that writes a str"""


def write_file(filename="", text=""):
    """writes a str
    filename: Filename
    return: number of characters
    """

    with open(filename, mode="w", encoding='utf-8') as my_file:
        return(my_file.write(text))
