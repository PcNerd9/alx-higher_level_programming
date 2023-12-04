#!/usr/bin/python3

"""
contain only one class:
    MyInt: inherit from the int
    object and invert the == and !=
    operator
"""


class MyInt(int):
    """
    inherit from int:
    and invert the == and != operator
    """
    def __eq__(self, other_number):
        return super().__ne__(other_number)

    def __ne__(self, other_number):
        return super().__eq__(other_number)
