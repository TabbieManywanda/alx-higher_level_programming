#!/usr/bin/python3
"""Writes a string to a text file and returns
number of characters written"""


def write_file(filename="", text=""):
    """A function that writes a string to
    a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text "\n")
