#!/usr/bin/python3
"""
An empty class
"""


class BaseGeometry:
    """
    Class that defines basic geometries.
    """
    def area(self):
        """
        raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        public instance method that validates value
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
