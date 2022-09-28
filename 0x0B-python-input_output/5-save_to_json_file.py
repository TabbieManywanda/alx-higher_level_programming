#!/usr/bin/python3
"""A function that writes an object to
a text file using JSON representation"""


def save_to_json_file(my_obj, filename):
    """Writes object to text file"""
    import json

    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, filename)
