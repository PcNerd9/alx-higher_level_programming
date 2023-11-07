#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == None:
        return
    for row in matrix:
        len_row = len(row)
        for i in row:
            if i != (row[len_row - 1]):
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i))
