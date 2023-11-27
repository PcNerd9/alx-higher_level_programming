#!/usr/bin/python3

"""
This module is a simple module that contains only
one function which compute the sum of two numbers
>>> add_integer(2, 5)
7
>>> add_integer(-2, 5)
3
"""


def add_integer(a, b=98):
    """ Compute the sum of two numbers
    >>> add_integer(2, 2.0)
    4
    """
    if (type(a) != int and (type(a) != float)):
        raise TypeError("a must be an integer or float")
    elif (type(b) != int and (type(b) != float)):
        raise TypeError("b must be an integer or float")
    else:
        return (int(a) + int(b))
