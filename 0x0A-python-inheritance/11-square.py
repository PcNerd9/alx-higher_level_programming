#!/usr/bin/python3

"""
contain only one class:
    Square: model the real
    life square shape and it
    inherit from the Rectangle
    class
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    model t he real life square shape and it
    inherit from the Rectangle
    class
    """
    def __init__(self, size):
        super().__init__(size, size)
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size <= 0):
            raise ValueError("size must be greater than 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
