#!/usr/bin/python3
"""
File Input Output Module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object
    to a text file, using a JSON representation:
    """
    with open(filename, "w") as file:
        return file.write(json.dumps(my_obj))
