#!/usr/bin/python3
"""
A class that defines a rectangle
"""


class Rectangle:
    """
    A class variable, counting the number of instances
    """
    number_of_instances = 0
    """
    a private instance attribute containing width and height
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
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
    """
    a public instance method that returns the area of a rectangle
    """
    def area(self):
        return self.__width * self.__height
    """
    a public instance method that returns the perimeter of a rectangle
    """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
    """
    a public instance method that prints in stdout the rectangle with #
    """
    def __str__(self):
        x = ""
        d = ["#" for c in range(int(self.__width))]
        a = "".join(d)
        for i in range(int(self.__height)):
            if self.__height == 0 or self.__width == 0:
                return ""
            if i < self.__height - 1:
                x += a + "\n"
            else:
                x += a
        return x
    """
    a public instance method
    """
    def __repr__(self):
        k = ""
        k += "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return k
    """
    deleting an instance
    """
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
