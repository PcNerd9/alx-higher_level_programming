#!/usr/bin/python3

"""
contain only one class:
    Student: initialize with first_name,
    last_name and age attributes
    contain tthe following methods:
    to_json: returnt the a dictionary
    representation of a student instance

    reload_from_json: replaces all attributes of the student
    instance
"""


class Student:
    """
    initializes with first_name, last_name and age
    contain the following methods
    to_json: returns the dictionary
    representaion of a student instance

    reload_from_json: replaces all attributes of the student
    instance
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs is None):
            return (self.__dict__)
        _dict = {}
        if (type(attrs) == str):
            if (attrs in self.__dict__):
                _dict[attrs] = self.__dict__[attrs]
                return (_dict)
        elif (type(attrs) == list):
            for att in attrs:
                if (att in attrs):
                    _dict[att] = self.__dict__[att]
            return (_dict)

    def reload_from_json(self, json):
        for key, value in json.items():
            if (key in self.__dict__):
                self.__dict__[key] = value
