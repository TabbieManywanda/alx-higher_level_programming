#!/usr/bin/python3
"""Funcion that returns dictionary description
for JSON serialization of an object"""


def class_to_json(obj):
    """Return dictionary description"""
    return obj.__dict__
