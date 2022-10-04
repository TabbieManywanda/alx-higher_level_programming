#!/usr/bin/python3
"""class Rectangle that inherits from Base"""


class Rectangle(Base):
    """class inheriting from another class Base;
    has private instance attributes each with its
    own getter and setter"""
    def __init__(self, width, height, x, y, id=None):
        """Initializing instance;
        calling super class for id argument if not
        passed in this particular class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.__height = value

    @property
    def x_value(self):
        """x getter"""
        return self.__x

    @x_value.setter
    def x_value(self, value):
        """x setter"""
        self.__x = value

    @property
    def y_value(self):
        """y getter"""
        return self.__y

    @y_value.setter
    def y_value(self, value):
        """y setter"""
        self.__y = value
