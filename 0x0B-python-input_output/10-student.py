#!/usr/bin/python3
"""class Student defined"""


class Student:
    """class with public instance attributes:
    firstname, lastname and age and a public method
    that retrieves a dictionary representation of a
    Student instance"""
    def __init__(self, first_name, last_name, age):
        """Initializing Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation
        of a Student instance"""
        if attrs is None:
            return self.__dict__
        d = {}
        for x in attrs:
            try:
                d[x] = self.__dict__[x]
            except KeyError:
                pass
        return d
