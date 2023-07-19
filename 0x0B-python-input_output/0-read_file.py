#!/usr/bin/python3
"""
File Input Output Module
"""


def read_file(filename=""):
    """
    Write a function that reads a text file (UTF8) and prints it to stdout:
    """
    with open(filename) as f:
        print(f.read(), end="")
