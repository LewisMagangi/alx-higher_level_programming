#!/usr/bin/python3
""" Finds Peak values """


def find_peak(list_of_integers):
    """Finding the peak"""
    if len(list_of_integers) == 0:
        return None
    peak = binary_search(list_of_integers, 0, len(list_of_integers) - 1)
    return list_of_integers[peak]


""" binary search algorithim """


def binary_search(a, low, high):
    """Recursive binary searching of the peak"""
    if low >= high:
        return low
    mid = ((high - low) // 2) + low
    if a[mid] > a[mid + 1]:
        return binary_search(a, low, mid)
    else:
        return binary_search(a, mid + 1, high)
