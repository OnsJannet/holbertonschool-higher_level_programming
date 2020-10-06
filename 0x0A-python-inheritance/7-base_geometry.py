#!/usr/bin/python3
"""
BaseGeometry
"""


class BaseGeometry:
    """
    An class named BaseGeometry
    attr1(area): Raises an exception
    """

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Raises an Exception"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} <name> must be greater than 0".format(name))
