#!/usr/bin/python3
"""Deserializing a JSON string to Python object"""


def from_json_string(my_str):
    """Returns object"""
    import json
    return json.loads(my_str)
