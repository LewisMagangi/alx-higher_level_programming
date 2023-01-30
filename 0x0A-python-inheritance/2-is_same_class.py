#!/usr/bin/python3
"""
a function that checks if an object
is an instance of a specified class
"""


def is_same_class(obj, a_class):
    '''
    a function that returns True
    if the object is exactly an instance of the specified class
    otherwise False.
    '''
    return True if type(obj) is a_class else False

        
