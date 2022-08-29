#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    urefu = len(new_list) - 1

    if idx < 0 or idx > urefu:
        return new_list
    new_list[idx] = element
    return new_list
