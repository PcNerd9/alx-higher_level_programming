#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if (len(matrix)) == 0:
        return
    new_matrix = [[i**2 for i in row] for row in matrix]
    return (new_matrix)
