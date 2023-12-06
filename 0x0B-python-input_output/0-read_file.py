#!/usr/bin/python3

"""
contains only one function:
    read_file: read a text document
    @filename: the name of the file
"""


def read_file(filename=""):
    """
    read a text document
    @filename: the name of the file
    """
    if (filename == ""):
        return
    with open(filename, mode="r", encoding="utf-8") as my_file:
        read_data = my_file.read()
        print(read_data, end="")
