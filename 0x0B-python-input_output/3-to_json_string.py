#!/usr/bin/python3
"""
File Input Output Module
"""
import json


def to_json_string(my_obj):
    """
    a function that returns the JSON representation of an object (string):
    """
    return json.dumps(my_obj)
