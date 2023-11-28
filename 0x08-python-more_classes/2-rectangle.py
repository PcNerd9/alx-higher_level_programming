#!/usr/bin/python3

"""
This module contain a single class
Rectangle - a class that model the real
life rectangle and has height and width
it also have area and perimeter methods
"""


class Rectangle:
    """
    it model the real life rectangle object, it
    has height and width. It also have area and
    perimeter methods
    """

    def __init__(self, width=0, height=0):
        """
        initialize the width and height of the
        newly created object with some restriction
        """
        if (type(width) != int):
            raise TypeError("width must be an integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        self.__width = width
        if (type(height) != int):
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height


    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("heigth must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (2 * (self.__width + self.__height))
