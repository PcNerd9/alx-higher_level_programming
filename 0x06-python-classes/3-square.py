#!/usr/bin/python3


"""
Defines a square with a private
instance attribute and also compute
the area
"""


class Square:
    """defines a square and compute
    the current area of the square
    """
    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size ** 2)
