#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list.append(search)
        else:
            new_list.append(my_list[i])
    return (new_list)
