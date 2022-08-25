#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    newstring = ""
    for letter in str:
        if i != n:
            newstring += letter
        i += 1
    return newstring
