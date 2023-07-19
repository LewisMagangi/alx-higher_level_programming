#!/usr/bin/python3
"""
This module contains the class Rectangle.
"""
BaseGeometry = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """
    a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height: def __init__(self, width, height):
        """
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)

    def area(self):
        """
        Method to find the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        str() should return,
        the following rectangle description: [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
