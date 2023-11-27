#!/usr/bin/python3

"""
This module contain a single function
that print a square using #
>>> print_square(3)
###
###
###
"""


def print_square(size):
    """
    print a square of size 'size' using #
    >>> print_square(4)
    ####
    ####
    ####
    ####
    """
    if (type(size) != int):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    if (size == 0):
        print()
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
