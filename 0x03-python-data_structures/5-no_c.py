#!/usr/bin/python3
def no_c(my_string):
    newstring = ""

    for x in my_string:
        if x != 'c' and x != 'C':
            newstring += x
    return newstring
