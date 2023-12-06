#!/usr/bin/python3
"""
contain only one function:
    pascal_triangle: return a pascal
    triangle of lenght n

    @n: the lenght of the pascal
    triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists containing
    a pascal triangle
    @n: the lenght of the pascal triangle
    """
    if (n <= 0):
        return []
    triangle = []
    triangle.append([1])
    j = 1
    for i in range(1, n):
        tmp = []
        tmp.append(1)
        for k in range(j - 1):
            tmp.append(triangle[j - 1][k] + triangle[j - 1][k + 1])
        tmp.append(1)
        j += 1
        triangle.append(tmp)
    return (triangle)
