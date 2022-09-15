#!/usr/bin/python3
"""Defining a class Square having size attributes"""


class Square:
    """Privatizing size of the square"""
    def __init__(self, __size):
        self.__size = __size
