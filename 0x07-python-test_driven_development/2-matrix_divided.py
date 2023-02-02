#!/usr/bin/python3
"""
a function that divides all elements of a matrix.
"""
def matrix_divided(matrix, div):
    '''
    a function that divides all elements of a matrix.
    '''
    new_matrix = [[u for u in f] for f in matrix]
    if type(new_matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    list_len = len(new_matrix[0])
    for i in range(len(new_matrix)):
        if type(new_matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        elif len(new_matrix[i]) != list_len:
            raise TypeError("Each row of the matrix must have the same size")
        for x in range(len(new_matrix[i])):
            if type(new_matrix[i][x]) != int and type(new_matrix[i][x]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[i][x] /= div
            new_matrix[i][x] = round(new_matrix[i][x], 2)

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    return new_matrix
