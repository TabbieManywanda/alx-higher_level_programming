#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0 or a_dictionary is None:
        return None
    big = max(a_dictionary.values())
    for x, y in a_dictionary.items():
        if y == big:
            return x
