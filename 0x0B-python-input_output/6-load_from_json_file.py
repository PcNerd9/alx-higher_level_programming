#!/usr/bin/python3

"""
contain only one function:
    load_from_json: creates an object from a
    json file
    @filename: the name of the file
"""
import json


def load_from_json_file(filename):
    """
    creates an object from a json file
    @filename: the name of the file
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
