#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n = {}
    for i in a_dictionary:
        n[i] = 2 * a_dictionary.get(i)
    return n
