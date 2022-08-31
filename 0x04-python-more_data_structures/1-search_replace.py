#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []

    for x in my_list:
        if x == search:
            x = replace
        newlist.append(x)
    return newlist
