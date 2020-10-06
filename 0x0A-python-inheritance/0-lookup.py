#!/usr/bin/python3
"""
a function that returns the list available
attributes and methods of an objct
"""


def lookup(obj):
    """
    obj: Object
    return: the list of available attributes and methods of an objct
    """
    return dir(obj)
