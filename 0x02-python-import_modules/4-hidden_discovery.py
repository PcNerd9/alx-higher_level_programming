#!/usr/bin/python3

import hidden_4
import dir

if __name__ == "__main__":
    list_of_variable = dir(hidden_4)
    list_of_variable.sort()
    for variable in list_of_variable:
        if variable[0] != "_":
            print(variable)
