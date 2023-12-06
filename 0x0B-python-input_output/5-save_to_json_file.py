#!/usr/bin/python3

"""
contain only one function:
    save_to_json_file: write an object
    to a text file, using a Json representaion
    @filename: the name of the file to write to
    @my_obj: the object to write to the file
"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
