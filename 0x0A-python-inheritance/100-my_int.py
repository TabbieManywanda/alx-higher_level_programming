#!/usr/bin/python3
"""class inheriting from int but having ==
and != functionalities inverted"""


class MyInt(int):
    """class having == and != inverted"""
    def __init__(self, value):
        """Initializing an instance"""
        self.value == value

    def __eq__(self, other):
        """Defines what happens when you
        call the '==' operator"""
        return self.value != other

    def __ne__(self, other):
        """Defines what happens when you
        call the '!=' operator"""
        return self.value == other
