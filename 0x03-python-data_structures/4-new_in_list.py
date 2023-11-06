#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    len_list = len(my_list)

    if (idx < 0 or idx > len_list - 1):
        return (my_list)
    new_list = []
    for i in range(len_list):
        if (i != idx):
            new_list.append(my_list[i])
        else:
            new_list.append(element)
    return (new_list)
