#!/usr/bin/python3
"""This module creates the Square class that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class named Square
    Attributes:
    attr1(id): id of object
    attr2(width): square width
    attr3(height): square height
    attr4(x): number of spaces before square
    attr5(y): number of spaces before square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance of Square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns string representation of Square """
        return"[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)