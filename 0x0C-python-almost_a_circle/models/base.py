#!/usr/bin/python3
""" Module of Base """


from json import dumps, loads

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns json str rep of a dictionary """
        if list_dictionaries is None:
            return dumps([])
        return dumps(list_dictionaries)

