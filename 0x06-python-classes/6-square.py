#!/usr/bin/python3


"""
Defines a square with a private
instance attribute
"""


class Square:
    """ defines a square with a size property,
    compute the current area of the square,
    and print the square using # with it appropriate
    co-ordinate"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if (type(value) == tuple and len(value) == 2):
            if (value[0] < 0 or value[1] < 0):
                raise TypeError("position must be\
                        a tuple of 2 positive integers")
            else:
                position = value
        else:
            raise TypeError("position must be a tuple\
                    of 2 positive integers")

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if (self.__size == 0):
            print()
            return

        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print()
