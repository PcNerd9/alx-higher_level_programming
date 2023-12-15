#!/usr/bin/python3

"""
contain only one class:
    Base: this is the base of all the class
    to be created
    it is intialized with id attribute
""" 
import json
class Base:
    """
    it serves as the base of all the class
    to be created. it is initialized with
    id attribute
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if (id is None):
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        with open("{}.json".format(cls.__class.__name__), "w", encoding="utf-8") as file:
            json_list = []
            if (list_objs is None or len(list_objs) == 0):
                json.dump(json_list, file)
                return

            for list_ in list_objs:
                json_list.append(cls.to_json_string(list_))
            json.dump(json_list, file)
