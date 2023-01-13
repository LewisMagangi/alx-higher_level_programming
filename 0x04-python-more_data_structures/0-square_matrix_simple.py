#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def n(m):
        return m * m
    t = matrix[:]
    for i in range(len(t)):
        for x in range(len(t[i])):
            t[i][x] = n(t[i][x])
    return t
