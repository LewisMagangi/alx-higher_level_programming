#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    return [t if t != search else replace for t in my_list]
