#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        ldigit = number % 10
    elif number < 0:
        ldigit = (number % -10) * -1
    print("{}".format(ldigit), end='')
    return ldigit
