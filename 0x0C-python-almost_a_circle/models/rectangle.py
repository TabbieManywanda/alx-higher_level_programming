#!/usr/bin/python3
"""class Rectange that inherits from Base"""


class Rectangle(Base):
    """class iheriting from another class Base;
    has private instance attributes each with its
    own getter and setter"""
    def __init__(self, width, height, x, y, id=None):
        """Initializing instance;
        calling super class for id argument if not
        passed in this particular class"""
        if id is None:
            super().__init__(id)
        else:
            self.id = id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x_value(self):
        return self.__x

    @x_value.setter
    def x_value(self, value):
        self.__x = value

    @property
    def y_value(self):
        return self.__y

    @y_value.setter
    def y_value(self, value):
        self.__y = value
