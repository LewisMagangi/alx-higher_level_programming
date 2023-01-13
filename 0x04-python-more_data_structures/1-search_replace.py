#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    for i in range(0, len(my_list)):
        if my_list[i] == search:
            newlist.append(replace)
        elif my_list[i] != search:
            newlist.append(my_list[i])
    return newlist
