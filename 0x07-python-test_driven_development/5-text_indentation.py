#!/usr/bin/python3
"""Defining a function that prints out text with
2 new lines after . : ?
"""


def text_indentation(text):
    """Prints out text with 2 new
    lines after characters . : ?
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for letter in text:
        if letter == ".":
            print(letter)
            print()
        elif letter == "?":
            print(letter)
            print()
        elif letter == ":":
            print(letter)
            print()
        else:
            print(letter, end="")
