#!/usr/bin/python3
"""class with public instance method that raises
an exception"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")
