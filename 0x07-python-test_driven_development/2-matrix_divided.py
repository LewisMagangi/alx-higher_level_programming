#!/usr/bin/python3
"""
a function that divides all elements of a matrix.
"""
def matrix_divided(matrix, div):
    '''
    a function that divides all elements of a matrix.
    '''
    new_matrix = matrix[:]
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    list_len = len(matrix[0])
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        elif len(matrix[i]) != list_len:
            raise TypeError("Each row of the matrix must have the same size")
        for x in range(len(matrix[i])):
            if type(matrix[i][x]) != int and type(matrix[i][x]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[i][x] /= div
    
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    return matrix
