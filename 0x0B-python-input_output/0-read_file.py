#!/usr/bin/python3
"""Function that reads a text file
and prints it out to stdout"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read())
