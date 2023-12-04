#!/usr/bin/python3

"""
contain only one class:
    BaseGeometry: valide the value integer
    passed is true
"""


class BaseGeometry:
    """
    validate the value integer passed is true
    or not
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (type(value) != int):
            raise TypeError("<name> must be an integer".format(name))
        elif (value <= 0):
            raise ValueError("<name> must be greater than 0".format(name))
