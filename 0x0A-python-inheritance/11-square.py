#!/usr/bin/python3
"""
This module contains the class Rectangle.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    a class Square that inherits from Rectangle
    (9-rectangle.py). (task based on 10-square.py).
    """
    def __init__(self, size):
        """
        Instantiation with size: def __init__(self, size):
        """
        self.__size = size
        self.integer_validator('size', size)

    def area(self):
        """
        Method to find the area of a square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        str() should return,
        the following rectangle description: [Rectangle] <width>/<height>
        """
        return f"[Square] {self.__size}/{self.__size}"
