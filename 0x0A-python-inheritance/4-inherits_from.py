#!/usr/bin/python3
"""
a function that checks if the object is an instance of the
specified class
"""


def inherits_from(obj, a_class):
    """
    a function that Checks if obj is instance of a specified class
    obj: Object
    a_class: Class
    return: True if is exactly instance, False otherwise
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
