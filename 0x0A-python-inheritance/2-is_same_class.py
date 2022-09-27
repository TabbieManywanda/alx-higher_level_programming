#!/usr/bin/python3
"""Returns True if object is exactly an instance
of the specified class"""


def is_same_class(obj, a_class):
    """A function that returns True if obj is
    an instance of a_class:
    Args = obj, a_class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
