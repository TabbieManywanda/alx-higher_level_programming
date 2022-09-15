#!/usr/bin/python3
"""Size of square must be an integer otherwise an exception is raised.
Size has to be >= 0 or we get a ValueError"""


class Square:
    """A class having attributes of a square"""
    def __init__(self, __size=0):
        self.__size = __size

        try:
            if type(__size) is not int:
                print("size must be an integer")
            if __size < 0:
                print("size must be >= 0")
        except TypeError:
            print()
        except ValueError:
            print()
