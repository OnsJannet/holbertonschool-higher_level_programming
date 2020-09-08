#!/usr/bin/python3
def no_c(my_string):
    new_char = ""
    for unwanted_char in my_string:
        if unwanted_char != 'c' and unwanted_char != 'C':
            new_char += unwanted_char
    return new_char
