#!/usr/bin/python3
""" Rectangle Module"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes args
        width is the width of the rectangle
        height is the height of the rectangle
        x is a space
        y is a space
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of class rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of class rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns x of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x of class rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns y of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y of class rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """ Prints a rectangle  """
        for y_space in range(self.__y):
            print()
        for column in range(self.__height):
            for x_space in range(self.__x):
                print(" ", end='')
            for row in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """Returns the str representation of the Rectangle"""
        string = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return string

    def update(self, *args, **kwargs):
        """Returns Arguments"""
        update = ("id", "width", "height", "x", "y")
        length = len(args)
        if args:
            for i in range(length):
                setattr(self, update[i], args[i])
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key in update:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the rectangle's dict """
        r_dict = {'x': self.__x, 'y': self.__y, 'id': self.id,
                  'height': self.__height, 'width': self.__width}
        return r_dict
