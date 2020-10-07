#!/usr/bin/python3
"""
function that returns the dictionary description
with simple data structure
"""


def class_to_json(obj):
    """a fucntion that creats obj from JSON
    obj: object
    return: dict description of obj
    """
    return obj.__dict__
