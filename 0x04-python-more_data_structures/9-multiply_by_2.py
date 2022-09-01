#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    thisdict = a_dictionary.copy()
    for x, y in thisdict.items():
        y *= 2
        thisdict[x] = y
    return thisdict
