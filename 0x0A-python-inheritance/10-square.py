#!/usr/bin/python3

"""
contain only one class:
    Square: it model te real life
    square and it inherited from the
    Rectangle class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    it model the real life
    square shape and it inherited from the Rectangle
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
