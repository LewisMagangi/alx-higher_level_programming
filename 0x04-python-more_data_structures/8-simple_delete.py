#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for i in a_dictionary:
        new[i] = 2 * a_dictionary.get(i)
    return new
