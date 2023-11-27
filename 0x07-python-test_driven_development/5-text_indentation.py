#!/usr/bin/python3

"""
This module contain a single function:
text_indentation - the function print a text to the
stdout and put a new line after it come accros
['.', ':', '?'] any of the character in the list
for example
>>> text_indentation("I am going. To be the best.")
I am going.
<BLANKLINE>
To be the best.
<BLANKLINE>
"""


def text_indentation(text):
    """
    print a text to the stdout and put a new line after
    it come accross ['.', ':', '?'] any of the character
    in the list
    for example
    >>> text_indentation("I am going. To be the best.")
    I am going.
    <BLANKLINE>
    To be the best.
    <BLANKLINE>
    """
    dil = ['.', ':', '?']
    if (type(text) != str):
        raise TypeError("text must be a string")
    for char in text:
        print(char, end="")
        if (char in dil):
            print()
            print()
