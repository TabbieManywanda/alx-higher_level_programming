#!/usr/bin/python3
"""Size of square must be an integer otherwise an exception is raised.
Size has to be >= 0 or we get a ValueError"""


class Square:
    """A class having attributes of a square"""
    def __init__(self, __size=0):
        self.__size = __size

        if type(__size) is not int:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
