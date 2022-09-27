#!/usr/bin/python3
"""Returns True if object is an instance of a class
inherited from the specified class"""


def inherits_from(obj, a_class):
    """A function that returns True if obj is
    an instance of a class that inherited from a_class
    """
    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    else:
        return False
