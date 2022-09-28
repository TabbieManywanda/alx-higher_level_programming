#!/usr/bin/python3
"""Adds all arguments to a Python list and save
them to a file"""


import json
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    pylist = load_from_json_file(filename)
except:
    pylist = []

for x in argv[1:]:
    pylist.append(x)
save_to_json_file(pylist, filename)
