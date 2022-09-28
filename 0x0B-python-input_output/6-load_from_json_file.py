#!/usr/bin/python3
"""Function that creates an Object from
JSON file"""


def load_from_json_file(filename):
    """Creates object form JSON file"""
    import json

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
