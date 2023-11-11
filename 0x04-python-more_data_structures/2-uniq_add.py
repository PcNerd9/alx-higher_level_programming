#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list is None:
        return
    unique_element = set(my_list)
    unique_list = list(unique_element)
    result = 0
    for i in unique_list:
        result += i
    return result
