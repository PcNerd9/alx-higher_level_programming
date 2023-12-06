#!/usr/bin/python3

"""
contain only one function:
    append_write: append to a text document
    @filename: the name of the file
    @text: the text to append
"""


def append_write(filename="", text=""):
    """
    append to the end of the file
    @filename: the name of the file
    @text: the text to append
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
