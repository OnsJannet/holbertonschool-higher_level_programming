#!/usr/bin/python3
"""Defining a class (Square)"""


class Square:
    """Square class
    Attributes:
    (size): the size of the square"""
    def __init__(self, size):
        """size: size for __size attribute of instance class"""
        self.__size = size  # this attribute is private
