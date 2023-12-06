#!/usr/bin/python3

"""
contains only one function:
    write_file: write to a text document
    @filename: the name of the file
    @text: to text to write to the file
"""


def write_file(filename="", text=""):
    """
    write to a text document
    @filename: the name of the file
    @text: the text to write to the file
    """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        char_written = my_file.write(text)
    return (char_written)
