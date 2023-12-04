#!/usr/bin/python3

"""
contain only one class:
    Rectangle: represent the rectangle shape
    and it inherit from the BaseGeometry class
    it can only take positive integers for its height
    and width
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    represent the rectangle shape
    it can only accept positive integers for width
    and height
    """

    def __init__(self, width, height):
        if (type(width) != int):
            raise TypeError("width must be an integer")
        elif (width <= 0):
            raise ValueError("width must be greater than 0")
        if (type(height) != int):
            raise TypeError("height must be an integer")
        elif (height <= 0):
            raise ValueError("height must be greater than 0")
        self.__width = width
        self.__height = height
