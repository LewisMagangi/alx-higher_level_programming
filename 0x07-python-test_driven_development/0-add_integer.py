#!/usr/bin/python3
"""
a function that adds two intergers
"""
def add_integer(a, b=98):
    if type(a) == float or type(b) == float:
        a , b = int(a), int(b)
    return a + b
