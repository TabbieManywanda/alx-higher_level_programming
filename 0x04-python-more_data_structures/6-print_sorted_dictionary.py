#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    x = sorted(a_dictionary.items())
    for i, z in x:
        print("{}: {}".format(i, z))
