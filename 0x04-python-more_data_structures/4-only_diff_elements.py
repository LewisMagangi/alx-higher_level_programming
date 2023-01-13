#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    newlist = []
    secondlist = []
    for i in set_1:
        if i not in set_2:
            newlist.append(i)

    for x in set_1:
        if x not in set_1:
            secondlist.append(x)
    return newlist.append()
