#!/usr/bin/python3
"""Defining a class (Square)"""


class Square:
    """Square class
    Attributes:
    (size): the size of the square"""
    def __init__(self, size=0):
        """size: size for __size attribute of instance class"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # this attribute is private

    def area(self):
        return self.__size * self.__size
