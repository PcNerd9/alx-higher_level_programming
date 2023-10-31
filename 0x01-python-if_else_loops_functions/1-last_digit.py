#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    remainder = (-1 * number) % 10
else:
    remainder = number % 10
string = f"Last digit of {number} is {remainder}"
if remainder > 5:
    string = string + " " + "and is greater than 5"
elif remainder == 0:
    strings = string + " " + "and is 0"
elif remainder < 6 and not 0:
    string = string  + " " + "and is less than 6 and not 0"
print(string)
