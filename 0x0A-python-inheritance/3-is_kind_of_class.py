#!/usr/bin/python3
"""Returns True if object is an instance of a specified
class or of a class that is inherited"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class
    or a class inherited from it"""
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
