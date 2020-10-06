#!/usr/bin/python3
"""
a function that checks if the object is an instance of the
specified class
"""


def is_same_class(obj, a_class):
    """
    a function that Checks if obj is instance of a specified class
    obj: Object
    a_class: Class
    return: True if is exactly instance, False otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
