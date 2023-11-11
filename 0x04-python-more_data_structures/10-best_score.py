#!/usr/bin/python3

def best_score(a_dictionary):
    if (a_dictionary is None):
        return
    if (len(a_dictionary) == 0):
        return
    number = 0
    for key, value in a_dictionary.items():
        if (number == 0):
            max_number = value
            person = key
            number += 1
        else:
            if (value > max_number):
                person = key
    return (person)
