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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):    
    def __init__(self, width, height):
        """ Init Args:
        Widh : an integer
        height : an integer
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
