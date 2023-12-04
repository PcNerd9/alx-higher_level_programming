#!/usr/bin/python3

"""
contain only one class:
    MyList it inherit from the list object
"""


class MyList(list):
    """
    print the list object in sorted form
    """
    def print_sorted(self):
        new_list = []
        for i in self:
            new_list.append(i)
        for i in range(len(new_list)):
            for j in range(0, len(new_list) - 1 - i):
                if (new_list[j] > new_list[j + 1]):
                    tmp = new_list[j]
                    new_list[j] = new_list[j + 1]
                    new_list[j + 1] = tmp
        print(new_list)
