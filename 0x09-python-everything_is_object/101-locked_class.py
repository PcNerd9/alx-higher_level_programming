#!/usr/bin/python3
"""
contain a single class
LockedClass - prevent user from
dynamically creating a new instance
attribute
"""


class LockedClass:
    """
    Prevent user from dynamicall creating a new intance
    attribute
    """
    __slots__ = ("first_name")
