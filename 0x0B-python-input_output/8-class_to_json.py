#!/usr/bin/python3

"""
contain only one function:
    class_to_json; returns a dictionary description
    with simple data structure(list, dictionay, string
    integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """
    returns a dictionary description with simple data structure(list, dictionary
    string integer and boolean) for Json serialization
    of an object
    """
    try:
        obj_dict = obj.__dict__
    except AttributeError:
        return(obj)
    dict_ = {}
    for key, value in obj_dict.items():
        dict_[key] = value

    return (dict_)
