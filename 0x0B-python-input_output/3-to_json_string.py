#!/usr/bin/python3

"""
contain only one function:
    to_json_string: returns the json
    representation of an object
    @my_obj: the object
"""
import json


def to_json_string(my_obj):
    """
    returns the json representation of an
    object
    @my_obj:th object
    """
    return json.dumps(my_obj)
