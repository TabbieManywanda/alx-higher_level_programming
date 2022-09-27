#!/usr/bin/python3
"""A class MyList that inherits from list"""

class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """prints sorted list"""
        print(list.sort(self))
