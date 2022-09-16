#!/usr/bin/python3
"""Defining a class Square; printing out a square now added"""


class Square:
    """class Square"""
    def __init__(self, __size=0):
        self.__size = __size
        if __size < 0:
            raise ValueError("size must be >= 0")
        if type(__size) is not int:
            raise TypeError("size must be an integer")

    def area(self):
        return self__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if value < 0:
            raise ValueError("size must be >= 0")
        if type(value) is not int:
            raise TypeError("size must be an integer")

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
