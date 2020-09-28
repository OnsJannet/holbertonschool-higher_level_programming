#!/usr/bin/python3
"""Defining a class (Rectangle)"""


class Rectangle:

    """Rectangle class
    Attributes:
    @width: the width of the rectangle
    @height: the height of the rectangle
    @Area: Returns a rectangle's area
    @Primeter: returns a rectangle's premieter
    @number_of_instances: Increments new instance
    during init and decrement during del
    __init__ : Initializes attributes
    __str__: Defines Behavior during str() & print()
    __repr__:return a str rep of the rectangle
    __del__: used during deletion it print a msg"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Rectangle Instantiation """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

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
        """ prints in stdout the Rectangle with a given symbol """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle

        for height in range(self.__height):
            for width in range(self.__width):
                rectangle += str(self.print_symbol)
            rectangle += '\n'
        rectangle = rectangle[:-1]
        return rectangle

    def __repr__(self):
        """ returns a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ Print a message when an instance of Rectangle is deleted """
        Rectangle.number_of_instances -= 1
        return print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger rectangle or the first, if both are equal"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
