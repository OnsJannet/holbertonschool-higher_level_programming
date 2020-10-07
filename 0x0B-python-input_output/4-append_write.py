#!/usr/bin/python3
"""a function that appends a string"""


def append_write(filename="", text=""):
    """appends a str and return the numer of char added
    filename: Filename
    return: number of characters
    """

    with open(filename, mode="a", encoding='utf-8') as my_file:
        return(my_file.write(text))
