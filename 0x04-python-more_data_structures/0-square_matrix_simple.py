#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    return [[c**2 for c in row] for row in matrix]
