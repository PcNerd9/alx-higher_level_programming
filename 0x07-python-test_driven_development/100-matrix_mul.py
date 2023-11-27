#!/usr/bin/python3


"""
Contains a single function:
matrix_mul - compute the matrix multiplication
of two vector matrix
>>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
[[7, 10], [15, 22]]
    """


def matrix_mul(m_a, m_b):
    """
    compute the matrix multiplication of
    two vector matrix containing only integer
    of float and return the result
    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7, 10], [15, 22]]
    """
    if (type(m_a) != list):
        raise TypeError("m_a must be a list")
    elif (type(m_b) != list):
        raise TypeError("m_b must be a list")

    if (not all(isinstance(sublist, list) for sublist in m_a)):
        raise TypeError("m_a must be a list of lists")
    elif (not all(isinstance(sublist, list) for sublist in m_b)):
        raise TypeError("m_b must be a list of lists")

    if (m_a == [] or m_a == [[]]):
        raise ValueError("m_a can't be empty")
    elif (m_b == [] or m_b == [[]]):
        raise ValueError("m_b can't be empty")
    len_column_a = len(m_a[0])
    len_row_b = len(m_b)
    len_column_b = len(m_b[0])
    result_mul = []

    if (len_column_a != len_row_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for row_a in m_a:
        if (len_column_a != len(row_a)):
            raise TypeError("each row of m_a must be of the same size")
        j = 0
        tmp = []
        for k in range(len_column_b):
            i = 0
            result = 0
            for row_b in m_b:
                if (len_column_b != len(row_b)):
                    raise TypeError("each row of m_b must be of the same size")
                if (type(row_a[i]) != int and type(row_a[i]) != float):
                    raise TypeError("m_a should contain only " +
                            "integers or floats")
                elif (type(row_b[j]) != int and type(row_b[j]) != float):
                    raise TypeError("m_b should contain only " +
                              "integers or floats")
                result += row_a[i] * row_b[j]
                i += 1
            tmp.append(result)
            j += 1
        result_mul.append(tmp)

    return (result_mul)
