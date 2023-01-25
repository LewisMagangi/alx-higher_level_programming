#!/usr/bin/python3
"""
A class that defines a rectangle
"""


class Rectangle:
    """
    a private instance attribute named width
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    """
    a private instance method that retrieves the width of a rectangle
    """
    @property
    def width(self):
        return self.__width
    """
    a private instance method that sets the width of a rectangle
    """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    """
    a private instance method that retrieves the height of a rectangle
    """
    @property
    def height(self):
        return self.__height
    """
    a private instance method that sets the height of a rectangle
    """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
