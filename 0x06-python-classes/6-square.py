#!/usr/bin/python3
"""Adding position attribute to the class"""


class Square:
    """class Square"""
    def __init__(self, __size=0, __position=(0, 0)):
        self.__size = __size
        self.__position = __position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
