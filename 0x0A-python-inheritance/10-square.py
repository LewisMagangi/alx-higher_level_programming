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
        Instantiation with width and height: def __init__(self, width, height):
        """
        self.__size = size
        self.integer_validator('width', size)

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
        return f"[Rectangle] {self.__size}/{self.__size}"
