#!/usr/bin/python3
"""Python class rectangle having attributes added"""


class Rectangle:
    """Width and height have to be positive integers"""
    def __init__(self, width=0, height=0):
        """Initialising the class"""
        if width < 0:
            raise ValueError("width must be >= 0")
        elif type(width) is not int:
            raise TypeError("width must be an integer")
        else:
            self.__width = width

        if height < 0:
            raise ValueError("height must be >= 0")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        else:
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
