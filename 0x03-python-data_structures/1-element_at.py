#!/usr/bin/python3
def element_at(my_list, idx):
    urefu = len(my_list) - 1
    if idx < 0 or idx > urefu:
        return None
    x = my_list[idx]
    return x
