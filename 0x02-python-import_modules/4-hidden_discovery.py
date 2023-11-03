#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    list_of_variable = dir(hidden_4)
    for variable in list_of_variable:
        if variable[0] != "_" and variable[1] != "_":
            print(variable)
