#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        len_row = len(row)
        for i in row:
            if i != (row[len_row - 1]):
                print("{}".format(i), end=" ")
            else:
                print("{}".format(i))
