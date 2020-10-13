#!/usr/bin/python3
""" Module of Base """


from json import dumps, loads
import csv


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
            my_file.write(Base.to_json_string(n_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            dummy = cls(2, 5)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ writes the CSV string representation of list_objs to a file """
        n_list = []
        if list_objs:
            n_list = [data.to_dictionary() for data in list_objs]
        with open(cls.__name__ + '.csv', 'w', encoding='utf-8') as my_csv_file:
            my_csv_file.write(Base.to_json_string(n_list))

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes in CSV """
        try:
            with open(cls.__name__ + '.csv', 'r',
                      encoding='utf-8') as my_csv_file:
                n_list = []
                file_dict = my_csv_file.read()
                if file_dict is None or len(file_dict) == 0:
                    return []
                file_data = cls.from_json_string(file_dict)
                for dictionary in file_data:
                    instance = cls.create(**dictionary)
                    n_list.append(instance)
                return n_list
        except Exception:
            return []
