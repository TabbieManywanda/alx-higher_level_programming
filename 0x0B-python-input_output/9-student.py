#!/usr/bin/python3
"""class Student defined"""


class Student:
    """class with public instance attributes:
    firstname, lastname and age and a public method
    that retrieves a dictionary representation of a
    Student instance"""
    def __init__(self, first_name, last_name, age):
        """Initializing Student instance"""
        self.firstname = first_name
        self.lastname = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation
        of a Student instance"""
        self.__obj__
