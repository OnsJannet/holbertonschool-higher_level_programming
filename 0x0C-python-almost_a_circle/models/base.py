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

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves a json string to a json file """
        n_list = []
        file_name = cls.__name__ + '.json'
        if list_objs:
            n_list = [data.to_dictionary() for data in list_objs]
        with open(file_name, 'w', encoding='utf-8') as my_file:
            my_file.write(Base.to_json_string(new_list))

