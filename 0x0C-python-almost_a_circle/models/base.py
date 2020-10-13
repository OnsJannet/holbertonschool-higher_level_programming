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
            return loads([])
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
    def load_from_file(cls):
        """ returns a list of instances"""
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r', encoding='utf-8') as my_file:
                n_list = []
                file_dict = my_file.read()
                if file_dict is None or len(file_dict) == 0:
                    return []
                file_data = cls.from_json_string(file_dict)
                for dictionary in file_data:
                    instance = cls.create(**dictionary)
                    n_list.append(instance)
                return n_list
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the CSV string representation of list_objs to a file"""
        with open(cls.__name__ + ".csv", "w", newline='') as my_csv_file:
            if cls.__name__ == "Rectangle":
                components = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                components = ['id', 'size', 'x', 'y']
            csv_writer = csv.DictWriter(my_csv_file, fieldnames=components)
            csv_writer.writeheader()
            if list_objs is not None:
                for model in list_objs:
                    csv_writer.writerow(model.to_dictionary())
    @classmethod
    def load_from_file_csv(cls):
        if path.exists(cls.__name__ + ".csv") is False:
            return []
        with open(cls.__name__ + ".csv", "r", newline='') as my_file:
            listofinstances = []
            csv_reader = csv.DictReader(my_file)
            for row in reader:
                for key, value in row.items():
                    row[key] = int(value)
                listofinstances.append(cls.create(**row))
        return listofinstances

