#!/usr/bin/python3
"""Function that reads a text file
and prints it out to stdout"""


def read_file(filename=""):
    """Reads a text file and prints it
    to stdout"""
    tmp = filename
    with open("tmp", "r", encoding="utf-8") as f:
        print(f.read())
