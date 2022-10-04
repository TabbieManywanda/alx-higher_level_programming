#!/usr/bin/python3
"""The class that will manage id attribute in all future
classes to avoid duplication"""


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing instance"""
        if id is None:
            Base.__nb_objects =+ 1
            self.id = self.__nb_objects
        else:
            self.id = id
