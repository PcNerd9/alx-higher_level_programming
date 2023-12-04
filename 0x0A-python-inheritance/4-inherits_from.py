#!/usr/bin/python3

"""
contains only one function:
    inherits_from: Returns true if the object
    is an instance of a class that inherited
    frim the specified class otherwise return
    False
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a
    class that inherited from the specified class
    otherwise return False
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
