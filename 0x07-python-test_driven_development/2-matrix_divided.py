#!/usr/bin/python3
"""
a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    '''
    a function that divides all elements of a matrix.
    '''
    x = "matrix must be a matrix (list of lists) of integers/floats"
    new = [[u for u in f] for f in matrix]
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    if type(new) != list:
        raise TypeError(x)
    list_len = len(new[0])
    matrix_len = len(new)
    for i in range(len(new)):
        if type(new[i]) is not list:
            raise TypeError(x)
        elif len(new[i]) not in [matrix_len, list_len]:
            raise TypeError("Each row of the matrix must have the same size")
        for x in range(len(new[i])):
            if type(new[i][x]) not in [int, float]:
                raise TypeError(x)
            new[i][x] /= div
            new[i][x] = round(new[i][x], 2)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    return new
