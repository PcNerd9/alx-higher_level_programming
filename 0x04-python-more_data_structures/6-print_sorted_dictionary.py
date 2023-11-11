#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if (a_dictionary is None):
        return
    if (len(a_dictionary) == 0):
        return
    sort_dict = sorted(list(a_dictionary))
    for key in sort_dict:
        print("{}: {}".format(key, a_dictionary[key]))
