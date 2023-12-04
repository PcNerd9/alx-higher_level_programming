#!/usr/bin/python3

"""
contains only one function:
    is_kind_of_class: returns true if the obj
    is an instance of a_class
"""
def is_kind_of_class(obj, a_class):
    """
    Returns true if the obj is an instance of
    a_class
    """
    return isinstance(obj, a_class)
