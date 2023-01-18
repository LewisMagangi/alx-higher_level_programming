#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for i in range(len(a_dictionary) + 1):
        a_dictionary[key] = value
    return a_dictionary
