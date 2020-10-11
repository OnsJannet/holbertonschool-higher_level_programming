#!/usr/bin/python3
""" Module of Base """


class Base:
    """ 1st classs Base
    __nb_objects : a class attribute
    def __init__(self, id=None): a class constructor
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
