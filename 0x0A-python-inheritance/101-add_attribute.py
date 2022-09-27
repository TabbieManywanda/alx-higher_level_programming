#!/usr/bin/python3
"""Defining a function that adds new attribute
to object if possible"""


def add_attribute(*args):
    if "main" in str(type(args[0])):
        setattr(args[0], args[1], args[2])
    else:
        raise TypeError("can't add new attribute")
