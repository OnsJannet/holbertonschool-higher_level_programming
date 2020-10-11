#!/usr/bin/python3
""" Base"""


from models.base import Base

class Rectangle(Base):
    """Rectangle class inheriting from Base class"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes args
        width is the width of the rectangle
        height is the height of the rectangle
        x is x 
        y is y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y