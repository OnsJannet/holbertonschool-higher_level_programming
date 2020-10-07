#!/usr/bin/python3
"""a function that saves object to a file"""


class Student:
    """Class named Student
    first_name: the first name of a student
    last_name: the last name of a student
    age: the age of a student
    """
    def __init__(self, first_name, last_name, age):
        """Init an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of student"""
        return self.__dict__