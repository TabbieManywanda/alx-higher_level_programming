#!/usr/bin/python3
"""Adding a sub class Square that inherits from
class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a sub class Square
    inheriting from super class Rectangle"""
    def __init__(self, size):
        """Initializing instance, args =
        size"""
        BaseGeometry.integer_validator(self, "size", size)
        self.__size = size

    def __str__(self):
        """Description of the square"""
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2
