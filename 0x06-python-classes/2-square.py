#!/usr/bin/python3
class Square:
    """defines a square and checks if its a digit >= 0"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # this attribute is private
