#!/usr/bin/python3
"""class with public instance method that raises
an exception"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value: raises exceptions if
        value < 0 or is not int"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initializing instance:
        Args - width, height"""
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
