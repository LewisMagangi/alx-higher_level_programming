#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        if i is int:
            print("{}".format(i))
        else:
            raise Exception
