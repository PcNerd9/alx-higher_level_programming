#!/usr/bin/python3

def uppercase(str):
    upper_value = ""
    for char in str:
        if (char >= 'a' and char <= 'z'):
            upper_value = upper_value + "{:c}".format(ord(char) - 32)
        else:
            upper_value = upper_value + char
    print(upper_value)
