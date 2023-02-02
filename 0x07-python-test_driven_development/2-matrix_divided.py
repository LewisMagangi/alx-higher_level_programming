#!/usr/bin/python3
"""
a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    '''
    a function that divides all elements of a matrix.
    '''
    s = "matrix must be a matrix (list of lists) of integers/floats"
    new = [[u for u in f] for f in matrix]
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    if type(new) != list:
        raise TypeError(s)
    for i in range(len(new)):
        if type(new[i]) is not list:
            raise TypeError(s)
        elif len(new[i]) not in [len(new), len(new[0])]:
            raise TypeError("Each row of the matrix must have the same size")
        for x in range(len(new[i])):
            if type(new[i][x]) not in [int, float]:
                raise TypeError(s)
            new[i][x] /= div
            new[i][x] = round(new[i][x], 2)
    return new
