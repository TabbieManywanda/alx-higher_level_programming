#!/usr/bin/python3
"""Adds all arguments to a Python list and save
them to a file"""

import json
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add.item.json"
try:
    deserial = load_from_json_file(filename)
except FileNotFoundError:
    deserial = []
finally:
    for x in argv[1:]:
        deserial.append(str(x))
    save_to_json_file(deserial, filename)
