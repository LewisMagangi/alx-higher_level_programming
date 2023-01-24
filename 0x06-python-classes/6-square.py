#!/usr/bin/python3
"""
a class that defines a Square
"""


class Square:
    """
    a private instance with attributes named size and position
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
    """
    a private instance method that retrieves the position of a square
    """
    @property
    def position(self):
        return self.__position
    """
    a private instance method that sets the position of a square
    """
    @position.setter
    def position(self, value):
        if type(f) is not tuple or len(f) != 2 or type(f[0]) is not int or type(f[1]) is not int or f[0] <= 0 or f[1] <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = value
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
                j = [" " for a in range(self.__position[0])]
                d = ["#" for c in range(self.__size)]
                x = j + d
                print("".join(x))
