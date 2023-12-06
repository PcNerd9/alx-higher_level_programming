#!/usr/bin/python3
"""
contain only one class;
Student: it is initialized with first_name
last_name and age
"""


class Student:
    """
    it is initialized with first_name, last_name and
    age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs == None):
            return (self.__dict__)
        _dict = {}
        if (type(attrs) == str):
            if (arrts in self.__dict__):
                _dict[attrs] = self.__dict__[attrs]
                return (_dict)
        elif (type(attrs) == list):
            for att in attrs:
                if (att in self.__dict__):
                    _dict[att] = self.__dict__[att]
            return (_dict)
