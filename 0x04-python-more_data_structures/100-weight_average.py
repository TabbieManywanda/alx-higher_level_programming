#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    result1 = 0
    result2 = 0
    for i, z in my_list:
        result1 += i * z
        result2 += z
    return (result1 / result2)
