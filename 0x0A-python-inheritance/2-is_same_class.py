#!/usr/bin/python3

"""
it only contains one function:
    is_same_class: returns True if the object
    is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly
    an instance of the specified class
    """
    if (type(obj) is a_class):
        return True
    else:
        return False
