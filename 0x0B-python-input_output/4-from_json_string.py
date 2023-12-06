#!/usr/bin/python3

"""
contain only one function:
    from_json_string: returns an object
    represented by a json string
    @my_str: the string
"""
import json


def from_json_string(my_str):
    """
    returns an object represented
    by a Json string
    @my_str: the string
    """
    return json.loads(my_str)
