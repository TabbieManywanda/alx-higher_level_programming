#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = number % 10
state = "Last digit of {} is {}{}"

if(mod > 5):
    print(state.format(number, mod, " and is greater than 5"))
elif(mod == 0):
    print(state.format(number, mod, " and is 0"))
else:
    print(state.format(number, mod, " and is less than 6 and not 0"))
