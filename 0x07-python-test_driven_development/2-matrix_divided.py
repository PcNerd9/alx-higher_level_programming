#!/usr/bin/python3
"""
This module contain only one function
matrix_divided. which compute a matrix division
operation
>>> matrix_divided([[2, 4, 6, 8], [10, 12, 14, 16]], 2)
[[1, 2, 3, 4], [5, 6, 7, 8]]
"""


def matrix_divided(matrix, div):
    """
    Return a new matrix that contain the result of
    dividing matrix with div
    matrix is a list of lists of integers or float only
    and div is a non zero integer
    >>> matrix_divided([[6, 8, 10], [4, 6, 10]], 2)
    [[3, 4, 5], [2, 3, 5]]
    """
    if ((type(matrix) == list) and
        (all(isinstance(sublist, list) for sublist in matrix))):
        if (type(div) != int and type(div) != float):
            raise TypeError("div must be a number")
        elif (div == 0):
            raise ZeroDivisionError("division by zero")
        lenght = len(matrix[0])
        new_matrix = []
        for list_ in matrix:
            if (lenght != len(list_)):
                raise TypeError("Each row of the matrix " +
                        "must have the same size")
            tmp = []
            for i in list_:
                if (type(i) != int and type(i) != float):
                    raise TypeError("matrix must be a matrix " +
                    "(list of lists) of integers/floats")
                result = float(i) / div
                tmp.append(round(result))
            new_matrix.append(tmp)
    else:
        raise TypeError("matrix must be a matrix " +
                        "(list of lists) of integers/floats")
    return new_matrix
