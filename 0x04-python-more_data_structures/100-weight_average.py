#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    f = sum([q * m for q, m in my_list])
    w = sum([m for q, m in my_list])
    if not w:
        return 0
    return f/w
