#!/usr/bin/python3

Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size <= 0):
            raise ValueError("size must be greater than 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)
