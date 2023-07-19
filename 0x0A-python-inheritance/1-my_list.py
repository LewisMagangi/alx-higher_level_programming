#!/usr/bin/python3
"""
 a class MyList that inherits from list:
"""


class MyList(list):
    """
    a class MyList that inherits from list:
    """
    def print_sorted(self):
        """
        A public instance method that prints the list, sorted (ascending sort)
        """
        sorted_list = sorted(self)
        print(sorted_list)
