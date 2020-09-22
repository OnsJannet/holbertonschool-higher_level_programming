#!/usr/bin/python3
"""Defining a class (Square)"""


class Square:
    """Square class
    Attributes:
    (size): the size of the square
    """
    def __init__(self, size=0):
        """
        size: size for __size attribute of instance class
        """
        self.__size = size  # this attribute is private

    def area(self):
        """ this helps calculate the area of the square
        returns the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """returns the size of the class instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.__size > 0:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
