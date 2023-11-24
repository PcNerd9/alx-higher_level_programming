#!/usr/bin/python3


"""
Defines a square with a private
instance attribute
"""


class Square:
    """defines a square with a size property
    compute the current area of the square and
    print the square using #
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
