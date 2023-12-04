#!/usr/bin/python3

"""
contain only one class:
    Rectangle: represent the real life rectangle
    shape
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class model the real life
    rectangle shap.
    it has a method that compute the area
    and a magic method(__str__)for string
    representation
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
        self.__height = height
        self.__width = width

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height)
