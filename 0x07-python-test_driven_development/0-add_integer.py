#!/usr/bin/python3
"""
a function that adds two intergers
"""


def add_integer(a, b=98):
    '''
    Returns an integer: the addition of a and b
    '''
    x = [float, int]
    ta, tb = type(a), type(b)
    if ta not in x:
        raise TypeError("a must be an integer")
    elif tb not in x:
        raise TypeError("b must be an integer")
    elif ta == x[0] or tb == x[0]:
        a, b = int(a), int(b)
    return a + b
