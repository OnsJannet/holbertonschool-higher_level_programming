#!/usr/bin/python3
"""
BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry class"""
    def __init__(self, width, height):
        """
        Init Args:
        Widh : an integer
        height : an integer
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
