#!/usr/bin/python3

"""
contain only one function:
    add_attribute: adds a new attribute to
    an object if it's possible
"""


def add_attribute(obj, attribute, value):
    """
    adds a new attribute to an object if it's possible
    """
    if (hasattr(obj, "__dict__")):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
