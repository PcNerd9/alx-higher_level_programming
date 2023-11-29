#!/usr/bin/python3

"""
Contain a single class
Rectangle is a simple class
that model the rectangle object
with height and width
which can only be integer
"""


class Rectangle:
    """
    It is a simple class that model the
    rectangle object with height and width
    which can only be integer
    """
    def __init__(self, width=0, height=0):
        if (type(width) != int):
            raise TypeError("width must be an integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        self.__width = width
        if (type(height) != int):
            raise TypeError("height myst be an integer")
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
    
    def __str__(self):
        if (self.__height == 0 or self.__width == 0):
            return ""
        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            string += "\n"

        return (string[:-1])
