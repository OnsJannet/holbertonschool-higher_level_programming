#!/usr/bin/python3
"""This modle creates a class named Student"""


class Student:
    """Class named Student
    first_name: the first name of a student
    last_name: the last name of a student
    age: the age of a student
    """
    def __init__(self, first_name, last_name, age):
        """Initializes an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of student"""
        if attrs is None:
            return self.__dict__
        dictionary = {}
        for i in attrs:
            if i in self.__dict__.keys():
                dictionary[i] = self.__dict__[i]
        return dictionary
