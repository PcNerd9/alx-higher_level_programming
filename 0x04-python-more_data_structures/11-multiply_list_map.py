#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return (list(map(lambda i, n: i * n, my_list, [number] * len(my_list))))
