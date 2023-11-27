#!/usr/bin/python3

import numpy as np

"""
contain a single function:
lazy_matrix_mul - compute the matrix multiplication
of two matrix vector using numpy module
>>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
[[ 7, 10]
 [15, 22]]
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Compute the matrix multiplication
    of two vector matrix with the help of
    numpy module
    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[ 7, 10]
     [15, 22]]
    """
    array_a = np.array(m_a)
    array_b = np.array(m_b)
    mul = array_a.dot(array_b)
    return (mul)
