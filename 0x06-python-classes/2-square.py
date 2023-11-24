#!/usr/bin/python3


"""
Defines a square with a private
instance attribute
"""

class Square:
    """define a square with only positive
    integers"""
    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
