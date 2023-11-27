#!/usr/bin/python3

"""
This module contain only one function
that print the full name
>>> say_my_name("Habeeb", "Ajayi")
My name is Habeeb Ajayi
"""


def say_my_name(first_name, last_name=""):
    """
    print a formated full name
    >>> say_my_name("Babatunde", "Ajayi")
    My name is Babatunde Ajayi
    """
    if (type(first_name) != str):
        raise TypeError("first_name must be a string")
    elif (type(last_name) != str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
