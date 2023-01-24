#!/usr/bin/python3
"""
a class that defines a Square
"""


class Square:
    """
    a private instance attribute named size
    """
    def __init__(self, size=0):
        self.__size = size
    """
    a private instance method that retrieves the size of a square
    """
    @property
    def size(self):
        return self.__size
    """
    a private instance method that sets the size of a square
    """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if int(value) < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """
    a public instance method that finds the area of a square
    """
    def area(self):
        area = self.__size ** 2
        return area
    """
    a public instance method that prints in stdout the square with #
    """
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                d = ["#" for c in range(self.__size)]
                print("".join(d))
