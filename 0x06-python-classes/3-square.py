#!/usr/bin/python3
"""
a class that defines a Square
"""


class Square:
    """
    a private instance attribute
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """
    public instance method that finds the area of a square
    """
    def area(self):
        area = self.__size ** 2
        return area
