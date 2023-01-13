#!/usr/bin/python3
def common_elements(set_1, set_2):
    x = []
    for i in list(set_1):
        if i in list(set_2):
            x.append(i)
    return set(x)
