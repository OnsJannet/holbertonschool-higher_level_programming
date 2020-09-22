#!/usr/bin/python3
"""Defining a class (Square)"""


class Square:
    """Square class
    Attributes:
    (size): the size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        size: size for __size attribute of instance class
        position: position for __position attribute of instance class
        """
        self.__size = size  # this attribute is private
        self.position = position

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
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for column in range(self.__position[0]):
                    print(" ", end="")
                for column in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def position(self):
        """returns the position of the class instance"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
