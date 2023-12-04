#!/usr/bin/python3

"""
Contains only one function:
    lookup: it return a list of all the attributes
    and methods in a class object
"""


def lookup(obj):
    """Return the list of all the attributes
    and methods present in a class object
    """
    return (dir(obj))
