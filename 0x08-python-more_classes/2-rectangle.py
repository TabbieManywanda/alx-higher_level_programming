#!/usr/bin/python3
"""class Rectangle with methods for area and perimeter"""


class Rectangle:
    """class Rectangle definition"""
    def __init__(self, width=0, height=0):
        """initializing class Rectangle:
        Arguments - weight and height"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @property
    """height getter method"""
    def height(self):
        return self.__height

    @width.setter
    """width setter method"""
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    """height setter method"""
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
