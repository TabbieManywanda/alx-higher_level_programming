#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tobedeleted = []
    for x, y in a_dictionary.items():
        if y == value:
            tobedeleted.append(x)
    for z in tobedeleted:
        del a_dictionary[z]
    return a_dictionary
