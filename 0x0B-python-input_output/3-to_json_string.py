#!/usr/bin/python3
"""Function that returns the JSON representation
of an object"""


def to_json_string(my_obj):
    """Returns JSON rep"""
    import json
    return json.dumps(my_obj)
