#!/usr/bin/python3
"""Building up on the class Square, now adding area"""


class Square:
    """Area of a square"""
    def __init__(self, __size=0):
        self.__size = __size

        if __size < 0:
            raise ValueError("size must be >= 0")
        if type(__size) is not int:
            raise TypeError("size must be an integer")

    def area(self):
        a = self.__size ** 2
        return a
