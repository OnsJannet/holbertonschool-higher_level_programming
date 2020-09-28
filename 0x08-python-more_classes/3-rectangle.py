#!/usr/bin/python3
"""Defining a class (Rectangle)"""


class Rectangle:
    """Rectangle class
    Attributes:
    @width: the width of the rectangle
    @height: the height of the rectangle"""

    def __init__(self, width=0, height=0):
        """ Rectangle Instantiation """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,value):    
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value # this attribute is private

    def height(self):
        """ this is the height of the Rectangle
        returns the height of the Rectangle
        """
        return self.__height 

    @property
    def height(self):
        """returns the height of the class instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle's area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns the Rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = self.__width * 2 + self.__height * 2
        return perimeter

    def __str__(self):
        """ prints in stdout the Rectangle with the character # """
        rectangle =""
        if self.__width == 0 or self.__height == 0:
            return rectangle

        for height in range(self.__height):
            for width in range(self.__width):
                rectangle += "#"
            rectangle += '\n'
        rectangle = rectangle[:-1]
        return rectangle
