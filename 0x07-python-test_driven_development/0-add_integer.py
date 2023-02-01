#!/usr/bin/python3
"""
a function that adds two intergers
"""


def add_integer(a, b=98):
    '''
    Returns an integer: the addition of a and b
    '''
    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    elif type(a) == float or type(b) == float:
        a, b = int(a), int(b)
    return a + b
