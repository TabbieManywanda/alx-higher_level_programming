#!/usr/bin/python3
"""Defining a function that returns the list of available
attributes and methods of an object"""


def lookup(obj):
    """Returns list of available attributes and methods
    in obj"""

    return dir(obj)
