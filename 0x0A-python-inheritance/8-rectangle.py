#!/usr/bin/python3
"""
This module contains the class Rectangle.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height: def __init__(self, width, height):
        """
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)
